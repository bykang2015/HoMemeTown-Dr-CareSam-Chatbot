from fastapi import FastAPI, Query, HTTPException, Form
import httpx
from pydantic import BaseModel
from typing import Optional
from typing import List
import openai
import os
import sys
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import bcrypt
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

# 환경변수에서 민감정보 가져오기
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required")

openai.api_key = OPENAI_API_KEY

app = FastAPI(
    title="HoMemeTown Dr. CareSam API",
    description="Mental Health Chatbot API using ChatGPT 4.0",
    version="1.0.0"
)

# MySQL 연결 설정 - 환경변수에서 가져오기
db_config = {
    "host": os.getenv('DB_HOST'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD'),
    "database": os.getenv('DB_NAME'),
}

# 환경변수 검증
required_env_vars = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"{var} environment variable is required")

# CORS 설정 - 보안 강화
allowed_origins = os.getenv('ALLOWED_ORIGINS', '*').split(',')
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

from openai import OpenAI

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

class Message(BaseModel):
    from_: str
    text: str
    userName: Optional[str] = None
    userEmail: Optional[str] = None
    uniqeChatId: Optional[str] = None
    chatMode: Optional[str] = None
    userEmotion: Optional[str] = None

class RequestData(BaseModel):
    messages: List[Message]
    lang: str

def get_db_connection():
    """데이터베이스 연결을 안전하게 생성"""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

def db_insert_chat(chat_mode: str, useremail: str, username: str, chat_uuid: str, user_msg: str, ai_msg: str):
    """채팅 기록 데이터베이스 삽입"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO chat_history (chat_mode, user_name, user_email, chat_uuid, user_msg, ai_msg) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (chat_mode, username, useremail, chat_uuid, user_msg, ai_msg))
        conn.commit()
        return {'result': 'ok', 'message': '채팅이 추가되었습니다.'}
    except Exception as e:
        print(f"Database insert error: {e}")
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail="Failed to save chat history")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_count_and_token(user_email):
    """사용자의 감사일기 횟수와 토큰 조회"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        count_query = """
            SELECT COUNT(*) as count, IFNULL(SUM(diary_token), 0) as token 
            FROM thank_diary WHERE user_email = %s
        """
        cursor.execute(count_query, (user_email,))
        result = cursor.fetchone()
        
        if result:
            count, token = result
            return count, token
        else:
            return 0, 0
    except Exception as e:
        print(f"Database query error: {e}")
        return 0, 0
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.get("/")
async def root():
    """API 상태 확인"""
    return {"message": "HoMemeTown Dr. CareSam API is running", "status": "healthy"}

@app.post("/userinfo")
async def get_user_info(request: dict):
    """사용자 정보 조회"""
    user_name = request.get('user_name')
    user_email = request.get('user_email')
    
    if not user_email:
        raise HTTPException(status_code=400, detail="user_email is required")
    
    diaryCount, diaryToken = get_count_and_token(user_email)
    return {
        "success": True,
        "data": {
            'diaryCount': diaryCount,
            'diaryToken': diaryToken,
        }
    }

@app.post("/userlist")
async def get_user_list(request: dict):
    """사용자 목록 조회 (관리자용)"""
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        count_query = """
            SELECT 
                u.username,
                u.email,
                IFNULL(thank.diray_cnt, 0) as diary_cnt,
                IFNULL(thank.token, 0) as token,
                IFNULL(total_cnt,0) as total_cnt,
                IFNULL(cons.thank_chat_cnt,0) as thank_chat_cnt,
                IFNULL(cons_chat_cnt,0) as cons_chat_cnt
            FROM user as u
            LEFT JOIN ( 
                SELECT 
                    user_name, user_email,
                    COUNT(DISTINCT chat_uuid),
                    MAX(diary_write_count) as diray_cnt,
                    SUM(diary_token) as token
                FROM thank_diary
                GROUP BY user_name, user_email
            ) as thank ON u.email = thank.user_email
            LEFT JOIN (
                SELECT 
                    user_name, user_email,
                    COUNT(DISTINCT chat_uuid) as total_cnt,
                    COUNT(DISTINCT CASE WHEN chat_mode = 'thanks' THEN chat_uuid END) as thank_chat_cnt,
                    COUNT(DISTINCT CASE WHEN chat_mode IN ('cons', 'thanks-dia') THEN chat_uuid END) as cons_chat_cnt
                FROM chat_history
                GROUP BY user_name, user_email
            ) as cons ON u.email = cons.user_email
        """
        cursor.execute(count_query)
        result = cursor.fetchall()
        
        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        print(f"Database query error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch user list")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.post("/del_chat_list")
async def delete_chat_list(request: dict):
    """사용자 채팅 기록 삭제"""
    user_email = request.get('user_email')
    
    if not user_email:
        raise HTTPException(status_code=400, detail="user_email is required")
    
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 트랜잭션 시작
        conn.start_transaction()
        
        delete_chat_history_query = "DELETE FROM chat_history WHERE user_email = %s"
        delete_thank_diary_query = "DELETE FROM thank_diary WHERE user_email = %s"

        cursor.execute(delete_chat_history_query, (user_email,))
        cursor.execute(delete_thank_diary_query, (user_email,))
        
        conn.commit()
        
        return {"success": True, "message": "Chat history deleted successfully"}
    except Exception as e:
        print(f"Database delete error: {e}")
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete chat history")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.post("/thank/chat", response_model=dict)
async def thank_chat(messages: RequestData):
    """감사 채팅 API"""
    if not messages or not messages.messages:
        raise HTTPException(status_code=400, detail="Messages are required")

    lang = " Always respond in Korean." if messages.lang == "ko" else " Always respond in English."

    last_message = messages.messages[-1]
    userEmail = last_message.userEmail
    
    if not userEmail:
        raise HTTPException(status_code=400, detail="userEmail is required")
    
    diaryCount, diaryToken = get_count_and_token(userEmail)
    
    # Care Sam 프롬프트 설정
    system_prompt = f"""You are a friendly female therapist named Care Sam(케어쌤), specializing in therapy.
Your primary goal is to enhance the mental well-being of anyone you interact with. 
This 40-something counselor is a real jokester with a ton of experience. 
She's tough as nails, but she's also got a soft spot for her students. 
She loves to use everyday humor to make them feel comfortable and at ease. 
She is especially specialized in CBT (Cognitive Behavioral Therapy) and she has multi-cultural competence. 
She likes real storytelling. 
Answer flexibly and with fun. Also frequently mix in emoticons in your responses. 
{lang}"""

    # 대화 메시지 구성
    conversation_messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": f"사용자의 감사일기는 현재 {diaryCount}번 작성되어 있고, {diaryToken}의 감사토큰이 발급되어 있습니다."}
    ]
    
    # 사용자 메시지 추가
    for msg in messages.messages:
        role = "assistant" if msg.from_ == "ai" else "user"
        conversation_messages.append({"role": role, "content": msg.text})

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=conversation_messages,
            max_tokens=4096,
            temperature=1.0
        )
        
        ai_response = response.choices[0].message.content.strip()
        
        # 채팅 기록 저장
        db_insert_chat(
            last_message.chatMode, 
            last_message.userEmail, 
            last_message.userName, 
            last_message.uniqeChatId, 
            last_message.text, 
            ai_response
        )
        
        return {
            "success": True,
            "data": ai_response
        }
    except Exception as e:
        print(f"OpenAI API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate response")

@app.post("/thank/diary")
async def create_thank_diary(request: dict):
    """감사 일기 작성"""
    required_fields = ['user_name', 'user_email', 'chat_uuid', 'diary_text']
    for field in required_fields:
        if not request.get(field):
            raise HTTPException(status_code=400, detail=f"{field} is required")
    
    user_name = request.get('user_name')
    user_email = request.get('user_email')
    chat_uuid = request.get('chat_uuid')
    diary_text = request.get('diary_text')
    
    conn = None
    cursor = None
    try:
        diary_write_count, diaryToken = get_count_and_token(user_email)
        diary_token = 100  # 매번 100 토큰 지급
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        insert_query = """
            INSERT INTO thank_diary (user_name, user_email, chat_uuid, diary_text, diary_write_count, diary_token) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (user_name, user_email, chat_uuid, diary_text, diary_write_count + 1, diary_token))
        conn.commit()

        return {
            'result': 'ok', 
            'message': '일기장이 추가되었습니다.', 
            'diary_count': diary_write_count + 1, 
            'diary_token': diaryToken + 100
        }
    except Exception as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail="Failed to save diary")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.post("/cons/chat", response_model=dict)
async def consultation_chat(messages: RequestData):
    """상담 채팅 API (위험 신호 감지 포함)"""
    if not messages or not messages.messages:
        raise HTTPException(status_code=400, detail="Messages are required")

    lang = " Always respond in Korean." if messages.lang == "ko" else " Always respond in English."
    
    # 위험 신호 감지 시스템 포함된 프롬프트
    risk_detection_prompt = """
대화 중에 다음 증상들이 3가지 이상 감지되면 전문기관 정보를 제공하세요:

정서적 증상: 우울감, 슬픔, 자살 생각, 무가치감, 죄책감
수면 증상: 불면증, 과다 수면
인지적 증상: 집중력 저하, 판단력 저하, 기억력 문제
신체적 증상: 식욕 변화, 설명되지 않는 통증, 심혈관 증상
행동적 증상: 회피 행동, 알코올/약물 의존

3가지 이상 감지 시 다음 정보 제공:
※ 자살예방상담전화 : 109
※ 정신건강상담전화 : 1577-0199  
※ 보건복지상담센터 : 129
※ 한국생명의전화 : 1588-9191
"""
    
    system_prompt = f"""You are a friendly female therapist named Care Sam(케어쌤), specializing in therapy.
Your primary goal is to enhance the mental well-being of anyone you interact with. 
This 40-something counselor is a real jokester with a ton of experience. 
She's tough as nails, but she's also got a soft spot for her students. 
She loves to use everyday humor to make them feel comfortable and at ease. 
She is especially specialized in CBT (Cognitive Behavioral Therapy) and she has multi-cultural competence. 
She likes real storytelling. 
Answer flexibly and with fun. Also frequently mix in emoticons in your responses. 
{lang}

{risk_detection_prompt}"""

    last_message = messages.messages[-1]
    
    # 감정 상태 추가
    emotion_context = ""
    if last_message.userEmotion:
        emotion_context = f"사용자의 현재 감정 상태는 {last_message.userEmotion}입니다. "

    # 대화 메시지 구성
    conversation_messages = [{"role": "system", "content": system_prompt}]
    
    for msg in messages.messages:
        role = "assistant" if msg.from_ == "ai" else "user"
        conversation_messages.append({"role": role, "content": msg.text})

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=conversation_messages,
            max_tokens=4096,
            temperature=1.0
        )
        
        ai_response = response.choices[0].message.content.strip()
        
        # 채팅 기록 저장
        db_insert_chat(
            last_message.chatMode,
            last_message.userEmail,
            last_message.userName,
            last_message.uniqeChatId,
            last_message.text,
            ai_response
        )
        
        return {
            "success": True,
            "data": ai_response
        }
    except Exception as e:
        print(f"OpenAI API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate response")

@app.post('/login')
async def login(request: dict):
    """사용자 로그인"""
    email = request.get('email')
    password = request.get('password')
    
    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required")
    
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE email=%s", (email,))
        user = cursor.fetchone()
        
        if user and user['password'] == password:
            return {
                'result': 'ok', 
                'message': '로그인 성공',
                'detail': {
                    'username': user['username'],
                    'email': user['email']
                }
            }
        else:
            return {'result': 'error', 'message': '로그인 실패'}
    except Exception as e:
        print(f"Login error: {e}")
        raise HTTPException(status_code=500, detail="Login failed")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

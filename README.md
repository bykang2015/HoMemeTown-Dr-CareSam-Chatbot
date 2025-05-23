# HoMemeTown Dr. CareSam Mental Health Chatbot

<div align="center">

![Dr. CareSam Logo](https://img.shields.io/badge/Dr.%20CareSam-Mental%20Health%20Chatbot-blue?style=for-the-badge)
![GPT-4](https://img.shields.io/badge/Powered%20by-ChatGPT%204.0-green?style=for-the-badge)
![Korean Support](https://img.shields.io/badge/Language-Korean%20%7C%20English-red?style=for-the-badge)

</div>

## 📄 논문 정보

**제목:** Development and Evaluation of a Mental Health Chatbot Using ChatGPT 4.0: Mixed Methods User Experience Study With Korean Users

**저자:** Boyoung Kang, ME, MBA; Munpyo Hong, PhD

**저널:** JMIR Medical Informatics 2025;13:e63538

**DOI:** [10.2196/63538](https://doi.org/10.2196/63538)

---

## 🤖 챗봇 개요

HoMemeTown Dr. CareSam은 **ChatGPT 4.0을 활용한 크로스링구얼 정신건강 지원 챗봇**입니다.

### ✨ 주요 특징
- 🌍 **이중언어 지원**: 영어/한국어 seamless 지원
- 🎭 **25개 감정 아이콘**: 시각적 감정 표현 시스템
- 📔 **감사 일기 기능**: 긍정적 사고 촉진
- 🚨 **위험 감지**: 리스크 키워드 모니터링 및 전문기관 연결
- 😊 **유머 기반 CBT**: 인지행동치료 + 일상적 유머

### 🎯 핵심 철학
> **"Your emotion is still valid"** - 모든 감정의 타당성 인정

---

## 🏗️ 시스템 아키텍처

### Frontend Development
- **React.js** framework for responsive user interface
- **Material-UI** component library for consistent design
- **WebSocket** implementation for real-time chat functionality
- **Client-side-only** session management with no persistent storage

### Backend Infrastructure
- **FastAPI** Python framework for high-performance API
- **Stateless architecture** with MySQL database
- **Direct API integration** with OpenAI's GPT-4
- **Environment-based configuration** for security

### OpenAI API Integration
- **GPT-4 Turbo** with custom prompt engineering
- **Conversation context management**
- **Response token limiting** for cost optimization
- **Risk detection and safety protocols**

---

## 📊 주요 기능

### 1. 🎭 감정 인식 시스템
- 25개 감정 몬스터 아이콘으로 시각적 감정 선택
- 선택된 감정에 맞춤형 응답 생성
- 감정 상태별 맞춤 상담 제공

### 2. 🌐 이중언어 대화 지원
- 영어/한국어 자동 감지 및 응답
- 문화적 맥락을 고려한 한국어 현지화
- Cross-lingual understanding 구현

### 3. 🚨 위험 감지 및 대응
**모니터링 증상:**
- 정서적: 우울감, 자살 생각, 무가치감
- 인지적: 집중력 저하, 판단력 문제
- 신체적: 수면 장애, 식욕 변화
- 행동적: 회피 행동, 물질 의존

**3가지 이상 감지 시 전문기관 정보 자동 제공:**
- 자살예방상담전화: 109
- 정신건강상담전화: 1577-0199
- 한국생명의전화: 1588-9191

### 4. 📔 감사 일기 & 토큰 시스템
- 감사 일기 작성으로 긍정적 사고 습관 형성
- 일기 작성마다 100 감사토큰 지급
- 사용자 동기 부여 및 지속 사용 촉진

---

## 📈 연구 결과

### 👥 연구 참여자
- **대상**: 한국 젊은 성인 20명 (18-27세, 평균 23.3세)
- **방법**: 혼합 연구방법론 (정량적 설문 + 정성적 피드백)

### 📊 사용성 평가 결과 (10점 만점)
| 평가 항목 | 평균 점수 | 표준편차 |
|-----------|-----------|----------|
| **긍정성 및 지지** | **9.0** ⭐ | 1.2 |
| **공감성** | **8.7** | 1.6 |
| **적극적 경청** | **8.0** | 1.8 |
| 전문성 | 7.0 | 2.0 |
| 개인화 | 7.4 | 2.4 |
| 복합성 | 7.4 | 2.0 |

### 🏆 비교 분석 결과
- **다른 LLM 챗봇 대비**: F=3.27, p=.047 (통계적 유의미한 차이)
- **Woebot/Happify 대비**: F=12.94, p<.001 (현저한 성능 우위)

---

## 🗂️ 저장소 구조

```
HoMemeTown-Dr-CareSam-Chatbot/
├── README.md                    # 메인 문서
├── backend/                     # FastAPI 백엔드 코드
│   ├── api.py                  # 메인 API 서버
│   ├── .env.example            # 환경변수 예시
│   ├── requirements.txt        # Python 패키지 목록
│   └── .gitignore             # Git 무시 파일
├── frontend/                    # React.js 프론트엔드 코드
│   └── (프론트엔드 파일들)
└── analysis/                    # 데이터 분석 노트북
    ├── Comparison_Chatbots.ipynb
    ├── Dr_CareSam_usability.ipynb
    └── README.md
```

---

## 🚀 설치 및 실행

### 백엔드 설정
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# .env 파일에 실제 API 키와 DB 정보 입력
python api.py
```

### 환경변수 설정
```bash
# .env 파일 생성 후 다음 정보 입력
OPENAI_API_KEY=your-openai-api-key
DB_HOST=your-database-host
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_NAME=your-database-name
```

---

## 🎯 핵심 혁신

### 1. 감정 아이콘 기반 UX
언어적 표현이 어려운 감정을 **시각적으로 선택**할 수 있는 직관적 인터페이스

### 2. 문화적 현지화
한국 대학생의 **문화적 맥락과 특성**을 반영한 공감적 응답 시스템

### 3. 프라이버시 우선 설계
대화 내용 선택적 저장으로 **사용자 프라이버시 보호**와 **학습 데이터 수집**의 균형

### 4. 즉시 안전망 연결
위기 상황 감지 시 **전문기관과 즉시 연결**하는 안전 시스템

---

## 🔒 보안 및 윤리

- **IRB 승인**: 성균관대학교 연구윤리위원회 승인
- **개인정보 보호**: Privacy by Design 원칙 준수
- **데이터 보안**: 환경변수 기반 민감정보 관리
- **투명성**: 오픈소스 코드 공개로 알고리즘 투명성 확보

---

## 🌟 주요 성과

### 학술적 기여
- **한국 최초** LLM 기반 정신건강 챗봇 개발 및 평가 연구
- **세계적으로 독특한** 3단계 검증 방법론 (디지털 테라피 → LLM 챗봇 → 비교 분석)
- **프롬프트 튜닝을 통한 AI 챗봇 맞춤 가능성** 입증

### 실용적 가치
- 대학생 정신건강 지원의 **접근성과 수용성** 향상
- **문화적 민감성**을 고려한 한국형 정신건강 도구 개발
- **유머와 공감을 통한 심리적 접근성** 향상 실증

---

## 🔮 향후 계획

### 단기 목표
- [ ] 더 큰 규모의 임상 시험 수행
- [ ] 위험 감지 기능 고도화
- [ ] 한국어 처리 성능 최적화

### 장기 비전
- [ ] 기존 의료 시스템과 통합
- [ ] 다양한 연령층으로 확장
- [ ] 글로벌 다국어 지원

---

## 📞 연락처

**교신저자:** 강보영 (Boyoung Kang)  
**이메일:** bykang2015@gmail.com  
**소속:** 성균관대학교  
**주소:** 서울특별시 종로구 성균관로 25-2

---

## 📄 인용

```bibtex
@article{kang2025chatbot,
  title={Development and Evaluation of a Mental Health Chatbot Using ChatGPT 4.0: Mixed Methods User Experience Study With Korean Users},
  author={Kang, Boyoung and Hong, Munpyo},
  journal={JMIR Medical Informatics},
  volume={13},
  pages={e63538},
  year={2025},
  publisher={JMIR Publications Inc.},
  doi={10.2196/63538}
}
```

---

## 🏷️ Keywords

`mental health chatbot` `Dr. CareSam` `HoMemeTown` `ChatGPT 4.0` `large language model` `LLM` `cross-lingual` `Korean students` `emotional AI` `digital therapy` `CBT` `humor therapy`

---

<div align="center">

**🌟 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요! 🌟**

</div># HoMemeTown-Dr-CareSam-Chatbot

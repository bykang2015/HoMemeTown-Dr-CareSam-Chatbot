# Analysis Code

## 📄 논문 정보
**제목:** Development and Evaluation of a Mental Health Chatbot Using ChatGPT 4.0: Mixed Methods User Experience Study With Korean Users

**저널:** JMIR Medical Informatics 2025;13:e63538

## 📊 분석 노트북 파일

### 1. Comparison_Chatbots.ipynb
- **목적:** LLM 기반 챗봇들 간의 성능 비교 분석
- **비교 대상:** 
  - HoMemeTown Dr. CareSam (우리 챗봇)
  - 기존 LLM 챗봇들 (Claude 3.5, ChatGPT 4.0)
  - 기존 디지털 치료 도구 (Woebot, Happify)
- **주요 결과:** 
  - 다른 LLM 챗봇 대비: F=3.27, p=.047
  - Woebot/Happify 대비: F=12.94, p<.001

### 2. Dr_CareSam_usability.ipynb
- **목적:** Dr. CareSam 챗봇의 사용성 평가 분석
- **참여자:** 20명 한국 젊은 성인 (18-27세)
- **평가 항목 (10점 만점):**
  - 긍정성 및 지지: 9.0 (SD 1.2)
  - 공감성: 8.7 (SD 1.6)
  - 적극적 경청: 8.0 (SD 1.8)
  - 전문성: 7.0 (SD 2.0)
  - 개인화: 7.4 (SD 2.4)

## 🛠 분석 환경
- **플랫폼:** Python
- **주요 라이브러리:** pandas, numpy, matplotlib, seaborn, scipy, sklearn

## 📈 주요 발견
1. **통계적 유의미한 성능 차이** 확인
2. **공감성과 지지 영역에서 높은 사용자 만족도**
3. **전문성과 개인화 영역의 개선 필요성** 확인

## 📞 문의
- **이메일:** bykang2015@gmail.com
- **소속:** 성균관대학교

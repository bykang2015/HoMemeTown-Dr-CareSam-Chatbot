# 📊 박사학위논문 실험 3: 정신건강 챗봇 상담학적 평가 가설검증

> **Dr.CareSam vs Global Mental Health Chatbots Comparative Analysis**  
> 박사학위논문의 실험 3에 대한 통계분석 코드

## 📋 개요

이 분석은 기존 JMIR MI 논문과는 **별개의 연구**로, 박사학위논문에서 닥터케어쌤의 글로벌 경쟁력을 검증하기 위한 실험 3의 4개 가설을 통계적으로 검증합니다.

### 🔬 연구 배경
- **기존 연구**: JMIR MI 논문 - 닥터케어쌤 개발 및 사용성 평가
- **이번 연구**: 박사논문 - 글로벌 정신건강 챗봇과의 상담학적 성능 비교

## 🎯 검증 가설

### H₁: 상담학적 평가 기준의 변별력
**실험 II에서 도출된 7가지 상담학적 평가 기준은 LLM 기반 평가 방법론을 통해 서로 다른 특성을 가진 정신건강 챗봇들 간의 상담적 품질 차이를 유의미하게 변별할 수 있을 것이다.**

### H₂: 닥터케어쌤의 글로벌 수준 성능  
**닥터케어쌤은 글로벌 수준의 정신건강 챗봇들과 대등한 상담적 성능을 보일 것이다.**

### H₃: LLM-인간 평가자 간 일치도
**LLM 평가자(Claude 3.5 Sonnet, ChatGPT 4.0)와 인간 전문가 간의 평가 결과는 중간 수준 이상의 일치도(r > 0.5)를 보일 것이다.**

### H₄: NLP vs 상담학적 평가의 차이
**전통적 NLP 평가 지표와 상담학적 평가 간에는 유의미한 차이가 나타날 것이다.**

## 📊 연구 설계

### 평가 대상 챗봇
- **Dr.CareSam** (국내 개발) - 본 연구에서 개발한 정신건강 챗봇
- **Wysa** (영국) - 글로벌 대표 정신건강 챗봇  
- **Youper** (미국) - AI 기반 정서 건강 챗봇
- **Replika** (미국) - 대화형 AI 동반자 챗봇

### 평가 기준 (7개)
1. **공감성** - 사용자 감정에 대한 이해와 공감 표현
2. **정확성과 유익성** - 정보의 정확성과 도움 정도
3. **목적적 사고와 감정** - 치료적 목적 달성을 위한 사고와 감정 유도
4. **적극적 경청과 적절한 질문** - 경청 자세와 치료적 질문
5. **긍정성과 지지** - 긍정적 지지와 격려
6. **전문성** - 정신건강 전문성 정도
7. **개인화** - 개별 사용자 맞춤형 대응

### 평가자 (3명)
- **Claude 3.5 Sonnet** - Anthropic의 LLM
- **ChatGPT 4.0** - OpenAI의 LLM  
- **Human Expert** - 정신건강 전문가

### 평가 척도
- **3점 척도**: 1점(낮음), 2점(중간), 3점(높음)
- **총 84개 평가점**: 7개 기준 × 3명 평가자 × 4개 챗봇

## 📈 주요 결과

### ✅ 모든 가설 채택

| 가설 | 결과 | 주요 통계량 |
|------|------|-------------|
| **H₁** | ✅ 채택 | F(3,80) = 9.73, p < 0.001, η² = 0.267 |
| **H₂** | ✅ 채택 | 닥터케어쌤 2위/4개 (평균 2.381) |
| **H₃** | ✅ 채택 | Cronbach's α = 0.837, LLM-인간 r > 0.5 |
| **H₄** | ✅ 채택 | 모든 NLP 지표 비유의 (p > 0.05) |

### 🏆 성능 순위
1. **Wysa**: 2.714점 (영국, 글로벌 1위)
2. **Dr.CareSam**: 2.381점 (한국, 글로벌 2위) 🇰🇷
3. **Youper**: 2.238점 (미국)  
4. **Replika**: 1.810점 (미국)

## 🔧 사용법

### 요구사항
```bash
pip install numpy pandas scipy matplotlib seaborn statsmodels
```

### 실행
```python
from phd_thesis_experiment3_analysis import PhDThesisExperiment3Analysis

# 분석 실행
analyzer = PhDThesisExperiment3Analysis()
results = analyzer.run_complete_analysis()
```

### 개별 가설 검증
```python
# 가설 1: 변별력 검증
h1_results = analyzer.hypothesis_1_discrimination_analysis()

# 가설 2: 닥터케어쌤 성능
h2_results = analyzer.hypothesis_2_drcare_performance()

# 가설 3: 평가자간 신뢰도
h3_results = analyzer.hypothesis_3_inter_rater_reliability()

# 가설 4: NLP vs 상담학적 평가
h4_results = analyzer.hypothesis_4_nlp_vs_counseling()
```

## 📁 파일 구조

```
analysis/
├── phd_thesis_experiment3_analysis.py    # 주 분석 코드
├── README.md                              # 이 파일
└── phd_thesis_experiment3_results.png     # 결과 시각화
```

## 📊 통계 분석 상세

### ANOVA (가설 1)
- **일원배치 분산분석**: 챗봇 간 유의한 차이 검증
- **사후검정**: Tukey HSD로 개별 비교
- **효과크기**: η² = 0.267 (큰 효과)

### 상관분석 (가설 3)
- **Pearson 상관계수**: 평가자 간 일치도 측정
- **내적 일관성**: Cronbach's α로 신뢰도 검증
- **기준**: r > 0.5 (중간 수준 이상 상관)

### 검정력 분석 (가설 4)
- **표본 크기**: n=4 (작은 표본의 한계)
- **임계값**: F(3,80, α=0.05) = 2.72, t(2, α=0.05) = 4.303
- **해석**: 실용적 유의성 중심 접근

## 🎓 학술적 기여

### 1. 방법론적 기여
- **LLM 기반 상담학적 평가 방법론** 개발 및 검증
- **다중 평가자 신뢰도 검증** 프레임워크 제시
- **전통적 NLP 지표의 한계** 실증적 규명

### 2. 실용적 기여  
- **국내 개발 챗봇의 글로벌 경쟁력** 실증
- **정신건강 챗봇 평가 기준** 표준화 기여
- **AI 기반 정신건강 서비스** 품질 보장 방안 제시

### 3. 정책적 시사점
- **국가 디지털 헬스케어** 경쟁력 강화 근거
- **AI 의료기기 인허가** 평가 기준 개발 기여
- **정신건강 서비스 접근성** 개선 방안 제시

## 📚 관련 논문

### 기 발표 논문
- **JMIR Medical Informatics** (Accepted, 2024)
  - "Development and Evaluation of a Mental Health Chatbot Using ChatGPT 4.0: Mixed Methods User Experience Study With Korean Users"

### 진행중 논문
- **박사학위논문** (In Progress, 2024)
  - 실험 3: 본 가설검증 분석 포함

## 👨‍💻 저자

**[Boyoung Kang]**

- GitHub: [@bykang2015](https://github.com/bykang2015)

## 📄 라이선스

이 프로젝트는 학술 연구 목적으로 공개되었습니다. 상업적 사용 시 저자에게 문의하시기 바랍니다.

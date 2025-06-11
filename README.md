# 🏥 HoMemeTown Dr. CareSam Mental Health Chatbot

> **종합 정신건강 챗봇 연구 프로젝트**  
> ChatGPT 4.0 기반 크로스링구얼 정신건강 지원 시스템

![DR. CARESAM](https://img.shields.io/badge/DR.%20CARESAM-MENTAL%20HEALTH%20CHATBOT-blue)
![POWERED BY](https://img.shields.io/badge/POWERED%20BY-CHATGPT%204.0-green)
![LANGUAGE](https://img.shields.io/badge/LANGUAGE-KOREAN%20%7C%20ENGLISH-red)

## 🔬 **연구 개요**

HoMemeTown Dr. CareSam은 **ChatGPT 4.0을 활용한 크로스링구얼 정신건강 지원 챗봇**으로, 한국 사용자를 대상으로 한 정신건강 서비스를 제공합니다. 본 프로젝트는 **개발부터 글로벌 경쟁력 검증**까지를 포괄하는 종합 연구입니다.

## 📚 **관련 연구 및 출판물**

### 1️⃣ **JMIR Medical Informatics (2025)** ✅ **Published**

**📄 논문 정보**
- **제목:** Development and Evaluation of a Mental Health Chatbot Using ChatGPT 4.0: Mixed Methods User Experience Study With Korean Users
- **저자:** Boyoung Kang, ME, MBA; Munpyo Hong, PhD
- **저널:** JMIR Medical Informatics 2025;13:e63538
- **DOI:** [10.2196/63538](https://doi.org/10.2196/63538)

**🎯 연구 목적:** 닥터케어쌤 개발 및 한국 사용자 대상 사용성 평가

**📁 관련 코드:** [`jmir-mi-paper/`](./jmir-mi-paper/)
- 챗봇 프론트엔드/백엔드 코드
- 사용성 평가 분석 코드
- 사용자 경험 연구 자료

---

### 2️⃣ **박사학위논문 (2024)** 🔬 **In Progress**

**📄 논문 정보**
- **제목:** [대학생 정신건강 증진을 위한 
디지털 중재 연구] 
- 대규모 언어 모델(LLM) 기반 대화형 AI 
상담 플랫폼의 설계와 실험적 평가 -

- **저자:** Boyoung Kang
- **기관:** [성균관 대학교]
- **상태:** 진행 중

**🎯 연구 목적:** 글로벌 정신건강 챗봇 대비 상담학적 성능 분석 및 경쟁력 검증

**📁 관련 코드:** [`phd-thesis/`](./phd-thesis/)
- 실험 3: 가설검증 통계분석
- 글로벌 챗봇 비교 연구
- LLM 기반 평가 방법론

## 🏆 **주요 연구 성과**

### **JMIR MI 논문 주요 결과**
- ✅ 한국어 정신건강 챗봇 성공적 개발
- ✅ 사용자 만족도 및 수용성 검증
- ✅ 크로스링구얼 대화 품질 확인

### **박사논문 주요 결과**
- 🥈 **글로벌 2위 성능** 달성 (Wysa > **Dr.CareSam** > Youper > Replika)
- ✅ **4개 가설 모두 채택** (통계적 유의성 확보)
- ✅ **LLM 평가 방법론** 타당성 검증

## 📁 **Repository 구조**

```
HoMemeTown-Dr-CareSam-Chatbot/
├── README.md                           # 이 파일
├── analysis/                           # JMIR MI 사용성 평가 분석
├── backend/                            # 챗봇 백엔드 (JMIR MI)
├── frontend/                           # 챗봇 프론트엔드 (JMIR MI)  
├── docs/                              # 문서화 (JMIR MI)
└── phd-thesis/                         # 🆕 박사논문 관련
    ├── experiment3-analysis/           # 실험 3 가설검증
    │   ├── hypothesis_testing.py       # 통계분석 코드
    │   └── README.md                   # 실험 3 상세 설명
    └── README.md                       # 박사논문 전체 개요
```

## 🚀 **Quick Start**

### **JMIR MI 논문 관련 코드 실행**
```bash
# 사용성 평가 분석
cd analysis/
# 챗봇 실행
cd backend/ # 또는 frontend/
# 상세 실행 방법은 각 폴더의 README 참조
```

### **박사논문 분석 코드 실행**
```bash
cd phd-thesis/experiment3-analysis/
python hypothesis_testing.py
# 상세 분석 방법은 phd-thesis/README.md 참조
```

## 🎯 **연구의 학술적 기여**

### **1. 방법론적 기여**
- **LLM 기반 상담학적 평가 방법론** 개발
- **다중 평가자 신뢰도 검증** 프레임워크
- **전통적 NLP 지표 한계** 실증적 규명

### **2. 실용적 기여**
- **국내 개발 챗봇의 글로벌 경쟁력** 실증
- **정신건강 서비스 접근성** 개선
- **AI 의료기기 평가 기준** 개발 기여

### **3. 정책적 시사점**
- **국가 디지털 헬스케어** 경쟁력 강화
- **AI 기반 정신건강 서비스** 품질 보장
- **정신건강 격차 해소** 방안 제시

## 👨‍💻 **연구진**

**주 연구자**
- **강보영 (Boyoung Kang)** - ME, MBA
  - 닥터케어쌤 개발 및 연구 총괄
  - GitHub: [@bykang2015](https://github.com/bykang2015)

**공동 연구자**
- **홍문표 (Munpyo Hong)** - PhD
  - 자문 및 피드백
  - 

## 📊 **인용 정보**

### **JMIR MI 논문 인용**
```bibtex
@article{kang2025development,
  title={Development and Evaluation of a Mental Health Chatbot Using ChatGPT 4.0: Mixed Methods User Experience Study With Korean Users},
  author={Kang, Boyoung and Hong, Munpyo},
  journal={JMIR Medical Informatics},
  volume={13},
  pages={e63538},
  year={2025},
  publisher={JMIR Publications},
  doi={10.2196/63538}
}
```

### **박사논문 인용**
```bibtex
@phdthesis{kang2024phd,
  title={[박사학위논문 제목]},
  author={Kang, Boyoung},
  year={2024},
  school={[소속 대학교]}
}
```

## 📄 **라이선스**

이 프로젝트는 학술 연구 목적으로 공개되었습니다. 상업적 사용 시 저자에게 문의하시기 바랍니다.

## 🙏 **감사의 말**

- **연구참여자**: 평가에 참여해주신 모든 사용자와 전문가분들
- **개발팀**: 닥터케어쌤 개발에 기여하신 모든 분들
- **학술 커뮤니티**: 소중한 피드백을 주신 연구자분들

---

**📞 문의사항이나 협업 제안은 언제든 환영합니다!**

**🔗 관련 링크**
- [JMIR MI 논문](https://doi.org/10.2196/63538)
- [개발자 GitHub](https://github.com/bykang2015)
- [프로젝트 이슈](https://github.com/bykang2015/HoMemeTown-Dr-CareSam-Chatbot/issues)

# NLP Teaching Multi-Agent System 🎓

자연어 처리 수업을 위한 Claude Code 기반 멀티 에이전트 시스템

## 🌟 주요 기능

### 1. Code Development Loop 💻
**3단계 자동 개선 시스템**
- **Implementer**: 코드 구현
- **Validator**: 테스트 및 검증
- **Debater**: 코드 리뷰 및 개선 제안
- 최대 3회 반복으로 고품질 코드 생산

### 2. NLP Knowledge Hub 📚
- NLP 이론 설명 (Transformer, Attention 등)
- 최신 논문 리뷰
- 웹 검색 (Tavily MCP)
- 한국어 NLP 특화

### 3. LaTeX Documentation ✍️
- 학술 문서 작성
- 수식 작성 (align, equation)
- BibTeX 참고문헌 관리
- TikZ 다이어그램

### 4. Tools & Infrastructure 🔧
- GitHub 버전 관리
- 데이터 전처리
- 실험 추적 (W&B, TensorBoard)
- 웹 검색

### 5. Teaching Assistant 🎯
- 쉬운 개념 설명
- 과제 힌트 제공
- 커리어 조언

## 📁 시스템 구조

```
.claude/
├── workspace/              # 작업 공간
│   ├── theory/            # 이론 학습 자료
│   ├── code/              # 코드 프로젝트
│   ├── documents/         # LaTeX 문서
│   └── data/              # 데이터셋
├── agents/
│   ├── supervisor.md      # 총괄 조정자
│   ├── pods/              # 5개 Pod
│   │   ├── nlp-knowledge/
│   │   ├── code-loop/
│   │   ├── latex-doc/
│   │   ├── tools/
│   │   └── teaching/
│   └── shared/
└── config/
    ├── system-config.yaml
    └── mcp-tools.yaml
```

## 🚀 사용 예시

### 예시 1: Transformer 구현
```
학생: "Transformer를 처음부터 구현하고 싶어요"

시스템 실행:
1. NLP Knowledge Hub
   → Transformer 이론 설명
   → Attention 논문 리뷰
   
2. Code Development Loop (3회 반복)
   Round 1: 초기 구현 → 버그 발견
   Round 2: 수정 → 테스트 통과
   Round 3: 최적화 → 승인
   
3. LaTeX Documentation
   → 구현 리포트 작성
   → 수식 및 다이어그램
   
4. GitHub
   → Repository 생성
   → README 작성

결과:
✅ transformer_v3.py (최적화된 코드)
✅ test_transformer.py (95% coverage)
✅ transformer_report.pdf (LaTeX 문서)
✅ GitHub: github.com/user/transformer-from-scratch
```

### 예시 2: 한국어 감정 분석
```
학생: "한국어 감정 분석 모델 만들고 싶어요"

시스템 실행:
1. 한국어 NLP 특성 조사 (병렬)
2. NSMC 데이터 전처리
3. KoBERT fine-tuning (Code Loop)
4. 실험 추적 (W&B)
5. 결과 문서화

결과:
✅ 정확도 88% 모델
✅ GitHub repo
✅ W&B 대시보드
✅ 프로젝트 리포트
```

## 🔑 핵심 특징

### ⭐ Code Development Loop
```
Implement → Validate → Debate → [Improve?]
     ↓          ↓          ↓
   v1.py    Test Results  Review
     ↓          ↓          ↓
   v2.py    ✅ Pass     Minor Issues
     ↓          ↓          ↓
   v3.py    ✅ Pass     ✅ Approve
```

**자동 개선 시스템**:
- 버그 발견 시 자동 재구현
- 최대 3회까지 개선
- 각 버전 테스트 및 리뷰

### 🎓 교육 맞춤
- **단계별 설명**: 쉬운 → 어려운
- **비유와 예시**: 직관적 이해
- **힌트 제공**: 답은 직접 주지 않음
- **피드백**: 격려와 건설적 제안

### ⚡ 병렬 실행
```
Task A: 이론 조사
Task B: 데이터 준비     } 동시 실행
Task C: 모델 조사
```

### 🔍 최신 정보
- Tavily MCP로 웹 검색
- arXiv, Hugging Face 조사
- 최신 논문 및 트렌드

## 📋 Requirements

```bash
# Python
Python 3.8+
PyTorch
transformers
numpy
pandas

# LaTeX
texlive-full

# Optional
Tavily API key
GitHub token
Hugging Face token
```

## 🛠️ 설정

1. **환경 변수**:
```bash
export TAVILY_API_KEY="your_key"
export GITHUB_TOKEN="your_token"
export HF_TOKEN="your_token"
```

2. **Claude Code 실행**:
```bash
# Supervisor와 대화 시작
claude code chat @supervisor

# 또는 직접 요청
claude code "Transformer 구현해주세요"
```

## 📚 문서

- `nlp-teaching-system-design.md`: 전체 시스템 설계 문서
- `.claude/agents/supervisor.md`: Supervisor 가이드
- `.claude/agents/pods/*/`: 각 Pod 문서

## 🎯 사용 시나리오

### 이론 학습
```
"Attention 메커니즘 설명해주세요"
→ 수식, 비유, 예시 포함 설명
```

### 코드 구현
```
"BERT fine-tuning 코드 작성해주세요"
→ Code Loop으로 고품질 코드 생성
```

### 과제 도움
```
"과제 막혔어요, 힌트 주세요"
→ 답은 주지 않고 방향 제시
```

### 프로젝트
```
"감정 분석 프로젝트 처음부터 끝까지"
→ 데이터 → 모델 → 평가 → 문서화 → GitHub
```

## 🤝 Contributing

이 시스템은 교육 목적으로 설계되었습니다.
개선 제안이나 버그 리포트는 환영합니다!

## 📄 License

MIT License

## 👥 Authors

NLP Teaching System Development Team

---

**Happy Learning! 🎓✨**

---

## 🔧 환경 변수 설정

### 빠른 시작

```bash
# 1. .env 파일 생성
cp .env.example .env

# 2. API 키 입력
nano .env  # 또는 선호하는 에디터

# 3. 설정 확인
python check_env.py
```

### 주요 환경 변수

```bash
# 웹 검색 (권장)
TAVILY_API_KEY=your_key_here

# GitHub 관리 (권장)
GITHUB_TOKEN=your_token_here
GITHUB_USERNAME=your_username
GITHUB_EMAIL=your_email@example.com

# Hugging Face (권장)
HF_TOKEN=your_token_here

# 실험 추적 (선택)
WANDB_API_KEY=your_key_here
```

### API 키 발급 방법

자세한 가이드: **[ENV_SETUP_GUIDE.md](ENV_SETUP_GUIDE.md)**

- **Tavily**: https://tavily.com (무료 월 1,000회)
- **GitHub**: Settings > Developer settings > Personal access tokens
- **Hugging Face**: https://huggingface.co/settings/tokens (무료)
- **W&B**: https://wandb.ai/authorize (무료)

### 설정 확인

```bash
# Python 스크립트로 확인
python check_env.py

# 출력 예시:
# 🔧 환경 변수 설정 상태
# ━━━━━━━━━━━━━━━━━━━━━━
# 📡 External API Keys:
#   TAVILY_API_KEY       : ✅ 설정됨
#   GITHUB_TOKEN         : ✅ 설정됨
#   HF_TOKEN             : ✅ 설정됨
#   WANDB_API_KEY        : ❌ 미설정
```

### 중요: 보안

- ⚠️ `.env` 파일은 **절대 Git에 커밋하지 마세요**
- ✅ `.gitignore`에 `.env`가 포함되어 있는지 확인
- ✅ `.env.example`은 템플릿용 (API 키 없음)

---

## 📁 프로젝트 구조 (상세)

```
nlp-teaching-system/
├── .env                      # 환경 변수 (Git 제외)
├── .env.example              # 환경 변수 템플릿
├── .gitignore                # Git 제외 목록
├── check_env.py              # 환경 변수 체크 스크립트
├── README.md                 # 이 파일
├── ENV_SETUP_GUIDE.md        # 환경 변수 설정 가이드
├── nlp-teaching-system-design.md  # 시스템 설계 문서
│
├── .claude/
│   ├── workspace/            # 작업 공간
│   │   ├── theory/          # 이론 학습 자료
│   │   ├── code/            # 코드 프로젝트
│   │   ├── documents/       # LaTeX 문서
│   │   └── data/            # 데이터셋
│   │
│   ├── agents/              # 에이전트 정의
│   │   ├── supervisor.md    # 총괄 조정자
│   │   ├── pods/            # 5개 전문 Pod
│   │   │   ├── nlp-knowledge/     # NLP 지식
│   │   │   ├── code-loop/         # 코드 개발 루프
│   │   │   ├── latex-doc/         # LaTeX 문서화
│   │   │   ├── tools/             # 도구 & 인프라
│   │   │   └── teaching/          # 교육 보조
│   │   └── shared/          # 공유 유틸리티
│   │
│   └── config/              # 설정 파일
│       ├── system-config.yaml     # 시스템 설정
│       └── mcp-tools.yaml         # MCP 도구 설정
│
└── utils/                   # 유틸리티
    ├── __init__.py
    └── env_loader.py        # 환경 변수 로더
```

---

## 🎯 다음 단계

### 1. 환경 설정
```bash
cp .env.example .env
nano .env  # API 키 입력
python check_env.py
```

### 2. 시스템 시작
```bash
# Supervisor와 대화
claude code chat @supervisor

# 또는 직접 요청
claude code "Transformer 구현해주세요"
```

### 3. 학습 시작!
```
"Attention 메커니즘 설명해주세요"
"BERT fine-tuning 코드 작성해주세요"
"한국어 감정 분석 프로젝트 도와주세요"
```


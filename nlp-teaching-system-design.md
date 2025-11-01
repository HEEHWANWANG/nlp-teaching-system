# NLP Teaching Multi-Agent System 🎓

자연어 처리 수업을 위한 멀티 에이전트 시스템 설계

## 시스템 개요

기존 neuro-ai-research-system을 기반으로 NLP 수업에 특화된 에이전트 시스템 구축:
- **코드 개발 & 검증 루프**: Implement → Validate → Debate
- **NLP 전문 지식**: 최신 NLP 이론 및 실무
- **LaTeX 문서화**: 수식 및 학술 문서 작성
- **GitHub 관리**: 버전 관리 및 협업
- **인터넷 검색**: Tavily MCP를 통한 최신 정보 수집

## Pod 구조 설계

### 📚 Pod 1: NLP Knowledge Hub (NLP 지식 센터)
**목적**: NLP 이론, 최신 연구, 실무 지식 제공

**Coordinator**: `nlp-knowledge-coordinator`

**전문 Agent들**:
1. **`@nlp-theory-agent`** 🎓
   - NLP 기초 이론 (tokenization, embeddings, attention 등)
   - 언어 모델 발전사 (RNN → Transformer → LLM)
   - 수학적 배경 (확률, 정보 이론, 최적화)
   
2. **`@nlp-papers-agent`** 📄
   - 최신 논문 검색 및 요약 (arXiv, ACL, EMNLP 등)
   - 논문 리뷰 및 핵심 아이디어 추출
   - 구현 가능한 아이디어 제안
   
3. **`@nlp-trends-agent`** 🔍
   - Tavily MCP 활용 인터넷 검색
   - Hugging Face, Papers with Code 최신 동향
   - 업계 트렌드 (LLM, RAG, Agent 등)
   
4. **`@linguistics-agent`** 🗣️
   - 언어학 지식 (형태론, 통사론, 의미론)
   - 다국어 처리 (한국어 특성)
   - 언어별 특수성 고려사항

**사용 시점**:
- 수업 주제 설명이 필요할 때
- 논문 리뷰 과제
- 새로운 기술 학습
- 과제 배경 지식 제공

---

### 💻 Pod 2: Code Development Loop (코드 개발 루프)
**목적**: Implement → Validate → Debate 순환을 통한 고품질 코드 개발

**Coordinator**: `code-loop-coordinator`

**전문 Agent들**:

1. **`@implementer-agent`** 🛠️
   - PyTorch/TensorFlow 코드 구현
   - Hugging Face Transformers 활용
   - 데이터 전처리 파이프라인
   - 모델 아키텍처 구현
   - SuperClaude Framework 통합
   
2. **`@validator-agent`** ✅
   - 코드 테스트 (unit test, integration test)
   - 성능 검증 (accuracy, F1, perplexity 등)
   - 메모리 및 속도 프로파일링
   - Edge case 테스트
   - 에러 핸들링 검증
   
3. **`@debater-agent`** 💬
   - 코드 리뷰 (PEP8, 가독성, 효율성)
   - 대안 제시 (다른 구현 방법)
   - 반론 제기 (잠재적 문제점)
   - 개선 제안 (최적화, 리팩토링)
   - 팀 토론 진행

**개발 루프 프로세스**:
```
사용자 요청 → Implementer (v1 구현)
              ↓
          Validator (테스트)
              ↓
          [Pass?]
         /      \
       No       Yes
      /           \
  Debater       완료
  (문제 지적)
      ↓
  Implementer (v2 구현)
      ↓
    (루프 반복 최대 3회)
```

**사용 시점**:
- 과제 코드 구현
- 논문 코드 재현
- 새로운 모델 개발
- 버그 수정

---

### 📝 Pod 3: LaTeX Documentation (학술 문서화)
**목적**: LaTeX 형식의 수식 및 문서 작성

**Coordinator**: `latex-doc-coordinator`

**전문 Agent들**:

1. **`@latex-writer-agent`** ✍️
   - LaTeX 문서 작성 (article, report, beamer)
   - 수식 작성 (align, equation, theorem 환경)
   - 알고리즘 의사코드 (algorithm2e)
   - 그림 및 표 삽입
   
2. **`@math-formula-agent`** 🔢
   - 수학 표기법 (notation) 통일
   - 복잡한 수식 LaTeX 변환
   - Attention 메커니즘 수식화
   - Loss function 수식 작성
   - 미분/적분 계산 및 표기
   
3. **`@biblio-agent`** 📚
   - BibTeX 참고문헌 관리
   - 논문 citation 자동 생성
   - Reference formatting (ACL, IEEE 등)
   - arXiv, DOI 자동 추가
   
4. **`@diagram-agent`** 🎨
   - TikZ 다이어그램 생성
   - 모델 아키텍처 그림
   - 어텐션 시각화
   - 흐름도 및 그래프

**사용 시점**:
- 과제 리포트 작성
- 논문 형식 문서 작성
- 수식이 포함된 설명
- 발표 자료 (Beamer)

**출력 예시**:
```latex
\documentclass{article}
\usepackage{amsmath, algorithm2e, tikz}

\begin{document}
\section{Attention Mechanism}
Self-attention은 다음과 같이 계산됩니다:
\begin{align}
    \text{Attention}(Q, K, V) &= \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \\
    \text{where } Q &= XW_Q, \quad K = XW_K, \quad V = XW_V
\end{align}
\end{document}
```

---

### 🔧 Pod 4: Tools & Infrastructure (도구 및 인프라)
**목적**: GitHub, 실험 관리, 데이터 처리 등 지원

**Coordinator**: `tools-coordinator`

**전문 Agent들**:

1. **`@github-manager-agent`** 🐙
   - Git 버전 관리
   - Branch 전략 (feature, develop, main)
   - PR 생성 및 리뷰
   - Issue 추적
   - GitHub Actions CI/CD
   
2. **`@data-engineer-agent`** 📊
   - 데이터셋 전처리 (cleaning, tokenization)
   - 데이터 증강 (augmentation)
   - 데이터 로더 구현
   - 데이터 통계 분석
   - 시각화 (matplotlib, seaborn)
   
3. **`@experiment-tracker-agent`** 🧪
   - 실험 설계 및 관리
   - 하이퍼파라미터 추적
   - 결과 로깅 (Weights & Biases, TensorBoard)
   - 모델 체크포인트 관리
   - 재현 가능성 보장
   
4. **`@web-researcher-agent`** 🌐
   - Tavily MCP 활용 검색
   - 기술 블로그 스크래핑
   - Hugging Face 모델/데이터셋 검색
   - Stack Overflow 솔루션 검색
   - 최신 튜토리얼 수집

**사용 시점**:
- 프로젝트 시작 (repo 설정)
- 데이터 준비
- 실험 진행 및 추적
- 최신 정보 필요 시

---

### 🎯 Pod 5: Teaching Assistant (교육 보조)
**목적**: 학생 맞춤형 교육 지원

**Coordinator**: `teaching-coordinator`

**전문 Agent들**:

1. **`@concept-explainer-agent`** 💡
   - 어려운 개념을 쉽게 설명
   - 비유 및 예시 제공
   - 단계별 학습 가이드
   - 퀴즈 및 연습 문제 생성
   
2. **`@homework-helper-agent`** 📖
   - 과제 힌트 제공 (답은 주지 않음)
   - 디버깅 도움
   - 개념 복습
   - 참고 자료 추천
   
3. **`@career-advisor-agent`** 🎓
   - NLP 커리어 패스 조언
   - 프로젝트 아이디어 제안
   - 포트폴리오 구성
   - 취업 준비 가이드

**사용 시점**:
- 수업 내용 질문
- 과제 막힐 때
- 진로 상담

---

## Supervisor: NLP Teaching Orchestrator

**역할**: 모든 Pod를 조율하는 중앙 컨트롤러

**핵심 기능**:
1. **사용자 요청 분석**: 질문 유형 파악 (이론, 코딩, 문서화 등)
2. **Pod 선택 및 조율**: 필요한 Pod/Agent 선택
3. **워크플로우 관리**: 순차/병렬 실행 결정
4. **외부 도구 중개**: API 호출 통합 관리
5. **진행 상황 보고**: 학생에게 명확한 피드백

**지원하는 외부 도구**:
- Claude API (Sonnet, Opus)
- Tavily MCP (웹 검색)
- GitHub API
- Hugging Face API
- arXiv API
- Weights & Biases API

---

## 워크플로우 예시

### 예시 1: "Transformer 모델을 처음부터 구현하고 싶어요"

```
Step 1: Supervisor 분석
├─ 이론 학습 필요: NLP Knowledge Hub
├─ 코드 구현 필요: Code Development Loop
├─ 문서화 필요: LaTeX Documentation
└─ GitHub 관리: Tools & Infrastructure

Step 2: NLP Knowledge Hub 가동
@nlp-theory-agent "Transformer 아키텍처 설명 (attention, positional encoding)"
@nlp-papers-agent "Attention is All You Need 논문 리뷰"
→ 출력: .claude/workspace/theory/transformer_explained.md

Step 3: Code Development Loop 시작

Round 1:
@implementer-agent "Transformer 구현 (encoder-decoder)"
→ 출력: transformer_v1.py

@validator-agent "테스트: forward pass, gradient flow"
→ 결과: ❌ positional encoding 버그 발견

@debater-agent "문제 분석 및 개선 제안"
→ 피드백: "sin/cos 주기 계산 오류, 차원 불일치"

Round 2:
@implementer-agent "버그 수정 (transformer_v2.py)"
@validator-agent "재테스트"
→ 결과: ✅ 통과

@debater-agent "코드 리뷰"
→ 피드백: "좋음! 추가 개선: multi-head attention 병렬화"

Round 3:
@implementer-agent "최적화 적용 (transformer_v3.py)"
@validator-agent "성능 테스트"
→ 결과: ✅ 속도 30% 향상

Step 4: LaTeX Documentation
@latex-writer-agent "구현 리포트 작성"
@math-formula-agent "Attention 수식 추가"
@diagram-agent "아키텍처 다이어그램"
→ 출력: transformer_report.tex

Step 5: GitHub Management
@github-manager-agent "repo 생성, 코드 커밋, README 작성"
→ GitHub URL: https://github.com/user/transformer-from-scratch

Step 6: 학생에게 보고
"Transformer 구현 완료! 🎉
 
📚 학습 자료:
  - 이론 설명: transformer_explained.md
  - 논문 리뷰: attention_is_all_you_need_review.md
  
💻 코드:
  - GitHub: https://github.com/user/transformer-from-scratch
  - 최종 버전: transformer_v3.py (3회 iteration)
  - 테스트 커버리지: 95%
  
📝 문서:
  - 리포트: transformer_report.pdf
  - 수식 및 다이어그램 포함
  
다음 단계:
  1. 데이터셋에서 학습 실험
  2. Pre-training 구현
  3. Fine-tuning 실습
  
어떤 걸 하시겠어요?"
```

### 예시 2: "한국어 감정 분석 모델 만들기 (처음부터 끝까지)"

```
Step 1: Supervisor 분석
├─ 한국어 특성 이해: Linguistics Agent
├─ 최신 모델 조사: Web Researcher
├─ 데이터 준비: Data Engineer
├─ 모델 구현: Code Development Loop
├─ 실험 추적: Experiment Tracker
└─ 결과 문서화: LaTeX Writer

Step 2: 병렬 실행 (동시에 3개 작업)

Task A: 배경 지식 수집
@linguistics-agent "한국어 형태소 분석, 조사/어미 처리"
@web-researcher-agent "Tavily 검색: 한국어 감정 분석 최신 연구"
→ 출력: korean_nlp_background.md

Task B: 데이터 준비
@data-engineer-agent "NSMC 데이터셋 다운로드 및 전처리"
@data-engineer-agent "데이터 분석: 클래스 불균형, 문장 길이 분포"
→ 출력: data_analysis.ipynb

Task C: 모델 아키텍처 조사
@nlp-papers-agent "KoBERT, KoELECTRA 논문 리뷰"
→ 출력: korean_pretrained_models.md

Step 3: 코드 개발 루프 (순차)

@implementer-agent "KoBERT fine-tuning 코드 작성"
@validator-agent "검증: 정확도 85% 달성"
@debater-agent "제안: 데이터 증강으로 성능 향상 가능"

@implementer-agent "back-translation 증강 추가"
@validator-agent "재검증: 정확도 88%"
@debater-agent "승인: 배포 가능"

Step 4: 실험 관리
@experiment-tracker-agent "W&B에 실험 결과 로깅"
→ W&B URL: https://wandb.ai/user/korean-sentiment

Step 5: 문서화
@latex-writer-agent "프로젝트 리포트 작성"
@math-formula-agent "Fine-tuning loss 수식 추가"
→ 출력: korean_sentiment_report.pdf

Step 6: GitHub 배포
@github-manager-agent "코드 정리 및 푸시"
@github-manager-agent "README.md 작성 (한/영)"
→ GitHub: https://github.com/user/korean-sentiment-analysis

최종 보고:
"한국어 감정 분석 프로젝트 완료! 🇰🇷

📊 성능:
  - Accuracy: 88%
  - F1-score: 0.87
  - 데이터: NSMC (15만 문장)
  
💡 배운 것:
  - 한국어 형태소 분석
  - KoBERT 활용
  - 데이터 증강 기법
  
📦 결과물:
  - GitHub repo (코드, 모델)
  - W&B 실험 대시보드
  - LaTeX 리포트
  
포트폴리오에 추가하시겠어요?"
```

---

## 파일 시스템 구조

```
.claude/
├── workspace/
│   ├── theory/              # 이론 학습 자료
│   │   ├── concepts/
│   │   ├── papers/
│   │   └── tutorials/
│   │
│   ├── code/                # 코드 프로젝트
│   │   ├── assignments/     # 과제
│   │   ├── projects/        # 프로젝트
│   │   └── experiments/     # 실험
│   │
│   ├── documents/           # LaTeX 문서
│   │   ├── reports/
│   │   ├── presentations/
│   │   └── notes/
│   │
│   └── data/                # 데이터셋
│       ├── raw/
│       ├── processed/
│       └── analysis/
│
├── agents/
│   ├── supervisor.md
│   │
│   ├── pods/
│   │   ├── nlp-knowledge/
│   │   │   ├── nlp-knowledge-coordinator.md
│   │   │   ├── nlp-theory-agent.md
│   │   │   ├── nlp-papers-agent.md
│   │   │   ├── nlp-trends-agent.md
│   │   │   └── linguistics-agent.md
│   │   │
│   │   ├── code-loop/
│   │   │   ├── code-loop-coordinator.md
│   │   │   ├── implementer-agent.md
│   │   │   ├── validator-agent.md
│   │   │   └── debater-agent.md
│   │   │
│   │   ├── latex-doc/
│   │   │   ├── latex-doc-coordinator.md
│   │   │   ├── latex-writer-agent.md
│   │   │   ├── math-formula-agent.md
│   │   │   ├── biblio-agent.md
│   │   │   └── diagram-agent.md
│   │   │
│   │   ├── tools/
│   │   │   ├── tools-coordinator.md
│   │   │   ├── github-manager-agent.md
│   │   │   ├── data-engineer-agent.md
│   │   │   ├── experiment-tracker-agent.md
│   │   │   └── web-researcher-agent.md
│   │   │
│   │   └── teaching/
│   │       ├── teaching-coordinator.md
│   │       ├── concept-explainer-agent.md
│   │       ├── homework-helper-agent.md
│   │       └── career-advisor-agent.md
│   │
│   └── shared/
│       ├── filesystem-manager.md
│       └── style-guide.md
│
└── config/
    ├── system-config.yaml
    └── mcp-tools.yaml
```

---

## 핵심 기능 요약

### 1. Code Development Loop ⭐
- **3단계 순환**: Implement → Validate → Debate
- **자동 개선**: 버그 발견 시 자동 재구현
- **품질 보장**: 테스트 커버리지 + 코드 리뷰

### 2. NLP 전문 지식 🧠
- 이론부터 최신 연구까지
- 한국어 NLP 특화 지원
- 논문 리뷰 및 구현 가이드

### 3. LaTeX 문서화 ✍️
- 수식 포함 학술 문서
- BibTeX 참고문헌 자동 관리
- 다이어그램 및 알고리즘 의사코드

### 4. GitHub 통합 🐙
- 버전 관리 자동화
- PR 및 이슈 추적
- CI/CD 파이프라인

### 5. 인터넷 검색 🔍
- Tavily MCP 활용
- 최신 기술 트렌드
- 튜토리얼 및 예제 코드

### 6. 교육 맞춤 지원 🎓
- 개념 설명 (쉬운 언어)
- 과제 힌트 (답은 안 줌)
- 진로 가이드

---

## 다음 단계

1. **에이전트 구현**:
   - 각 Pod의 Coordinator 및 Agent별 markdown 파일 작성
   - System prompt 및 persona 정의

2. **도구 통합**:
   - Tavily MCP 연결
   - GitHub API 설정
   - LaTeX 컴파일 환경

3. **테스트**:
   - 간단한 과제로 전체 루프 테스트
   - 병렬 실행 검증

4. **문서화**:
   - 사용자 가이드
   - API 레퍼런스

---

## 구현 우선순위

### Phase 1: 핵심 기능 (2주)
1. Supervisor
2. Code Development Loop (3 agents)
3. NLP Theory Agent
4. GitHub Manager

### Phase 2: 문서화 (1주)
1. LaTeX Writer
2. Math Formula Agent
3. Biblio Agent

### Phase 3: 고급 기능 (2주)
1. Web Researcher (Tavily MCP)
2. Experiment Tracker
3. Teaching Assistants

---

이 설계로 진행하시겠어요? 아니면 수정하고 싶은 부분이 있나요?

# 환경 변수 설정 가이드 🔧

## 빠른 시작

### 1. .env 파일 생성
```bash
# .env.example을 복사
cp .env.example .env

# .env 파일 편집
nano .env  # 또는 vim, code 등
```

### 2. API 키 발급 및 설정

#### 필수 아님, 하지만 권장하는 설정들:

```bash
# .env 파일에 다음과 같이 입력
TAVILY_API_KEY=tvly-xxxxxxxxxxxxx
GITHUB_TOKEN=ghp_xxxxxxxxxxxxx
HF_TOKEN=hf_xxxxxxxxxxxxx
WANDB_API_KEY=xxxxxxxxxxxxx
```

### 3. 설정 확인
```bash
# Python 스크립트로 확인
python check_env.py

# 또는 직접 테스트
python -c "from utils.env_loader import env; env.print_status()"
```

---

## 📡 API 키 발급 방법

### 1. Tavily API (웹 검색) 🔍

**용도**: 최신 NLP 트렌드, 논문, 튜토리얼 검색

**발급 방법**:
1. https://tavily.com 방문
2. Sign Up (무료)
3. Dashboard > API Keys
4. "Create API Key" 클릭
5. 키 복사

**무료 플랜**:
- 월 1,000회 검색 무료
- 충분히 학습용으로 사용 가능

**설정**:
```bash
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 2. GitHub Personal Access Token 🐙

**용도**: 자동 repository 생성, 코드 푸시, Issue 관리

**발급 방법**:
1. GitHub 로그인
2. Settings > Developer settings
3. Personal access tokens > Tokens (classic)
4. "Generate new token" 클릭
5. 권한 선택:
   - ✅ `repo` (전체)
   - ✅ `workflow`
   - ✅ `write:packages` (선택사항)
6. "Generate token" 클릭
7. 토큰 복사 (한 번만 보임!)

**설정**:
```bash
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
GITHUB_USERNAME=your_username
GITHUB_EMAIL=your_email@example.com
```

**주의**:
- 토큰은 비밀번호처럼 관리
- .env 파일을 절대 Git에 커밋하지 말 것
- .gitignore에 .env가 포함되어 있는지 확인

---

### 3. Hugging Face Token 🤗

**용도**: 모델/데이터셋 다운로드, Private repo 접근

**발급 방법**:
1. https://huggingface.co 로그인
2. Settings > Access Tokens
3. "New token" 클릭
4. 권한:
   - 읽기 전용: `read`
   - 업로드도 필요: `write`
5. 토큰 복사

**설정**:
```bash
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
HF_HOME=~/.cache/huggingface
```

**무료**:
- 공개 모델/데이터셋은 토큰 없이도 가능
- 토큰 있으면 속도 제한 완화
- Private repo 접근 가능

---

### 4. Weights & Biases API Key 📊

**용도**: 실험 추적, 하이퍼파라미터 비교, 결과 시각화

**발급 방법**:
1. https://wandb.ai 가입 (무료)
2. https://wandb.ai/authorize 방문
3. API Key 복사

**설정**:
```bash
WANDB_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WANDB_PROJECT=nlp-teaching-project
WANDB_ENTITY=your_username
```

**무료 플랜**:
- 무제한 개인 프로젝트
- 100GB 스토리지
- 학습용으로 충분

---

### 5. OpenAI API (선택사항)

**용도**: GPT 모델 사용 (이 시스템은 주로 Claude 사용)

**발급**:
1. https://platform.openai.com
2. API keys > Create new secret key

**설정**:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**비용**: 사용량에 따라 과금

---

### 6. Anthropic API (선택사항)

**용도**: Claude API 직접 호출

**발급**:
1. https://console.anthropic.com
2. API Keys > Create Key

**설정**:
```bash
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

## ⚙️ 시스템 설정

### Code Loop 설정

```bash
# 최대 반복 횟수 (기본: 3)
MAX_CODE_ITERATIONS=3

# 타임아웃 (초, 기본: 3600 = 1시간)
TASK_TIMEOUT=3600

# 병렬 작업 수 (기본: 3)
MAX_PARALLEL_TASKS=3
```

**권장**:
- 간단한 작업: `MAX_CODE_ITERATIONS=2`
- 복잡한 프로젝트: `MAX_CODE_ITERATIONS=5`
- 빠른 테스트: `TASK_TIMEOUT=600` (10분)

---

### 로깅 설정

```bash
# 로그 레벨
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
```

**DEBUG**: 모든 상세 로그 (디버깅 시)
**INFO**: 일반 정보 (권장)
**WARNING**: 경고만
**ERROR**: 에러만

---

### PyTorch 설정

```bash
# GPU 설정
CUDA_VISIBLE_DEVICES=0  # 첫 번째 GPU 사용
# CUDA_VISIBLE_DEVICES=0,1  # 2개 GPU 사용
# CUDA_VISIBLE_DEVICES=""  # CPU만 사용

# 모델 캐시
TORCH_HOME=~/.cache/torch
```

---

### LaTeX 설정

```bash
# 컴파일러 (기본값으로 충분)
LATEX_COMPILER=pdflatex
BIBTEX_COMPILER=bibtex
```

---

## 🔒 보안 Best Practices

### 1. .env 파일 관리

```bash
# ✅ 좋은 예
.env               # Git에서 제외됨
.env.example       # 템플릿 (Git에 포함)
.gitignore         # .env를 무시 목록에 추가

# ❌ 나쁜 예
.env를 Git에 커밋
API 키를 코드에 하드코딩
```

### 2. .gitignore 확인

```bash
# .gitignore에 반드시 포함
.env
*.env
!.env.example
```

### 3. API 키 관리

```bash
# ✅ 안전한 방법
export TAVILY_API_KEY=$(cat .env | grep TAVILY_API_KEY | cut -d '=' -f2)

# ❌ 위험한 방법
echo "my_api_key" > api_key.txt  # 파일로 저장
TAVILY_API_KEY=my_key  # 쉘 히스토리에 남음
```

### 4. 토큰 만료 및 순환

- GitHub 토큰: 90일마다 갱신 권장
- 의심스러운 활동 발견 시 즉시 재발급
- 오래된 토큰은 삭제

---

## 🧪 테스트 모드

개발 중이거나 API 비용이 걱정될 때:

```bash
# 테스트 모드 (실제 API 호출 안 함)
TEST_MODE=true
USE_MOCK_RESPONSES=true

# 개발 모드
DEV_MODE=true
DEBUG=true
```

**테스트 모드에서는**:
- API 키 없이도 작동
- Mock 데이터 사용
- 비용 발생 없음

---

## 📋 체크리스트

### 기본 설정 (필수)
- [ ] `.env` 파일 생성 (`cp .env.example .env`)
- [ ] `.gitignore`에 `.env` 포함 확인
- [ ] `check_env.py` 실행하여 상태 확인

### API 키 (권장)
- [ ] Tavily API (웹 검색용)
- [ ] GitHub Token (repo 관리용)
- [ ] Hugging Face Token (모델 다운로드용)
- [ ] W&B API Key (실험 추적용)

### 시스템 설정
- [ ] `MAX_CODE_ITERATIONS` 확인
- [ ] `CUDA_VISIBLE_DEVICES` 설정 (GPU 사용 시)
- [ ] `LOG_LEVEL` 설정

---

## 🔍 트러블슈팅

### Q1: "TAVILY_API_KEY not found" 에러

**원인**: API 키가 설정되지 않음

**해결**:
```bash
# .env 파일 확인
cat .env | grep TAVILY_API_KEY

# 키가 비어있으면
echo "TAVILY_API_KEY=your_key_here" >> .env

# 또는 .env 편집
nano .env
```

### Q2: GitHub 푸시가 안됨

**원인**: GitHub 토큰 권한 부족

**해결**:
1. GitHub Settings > Developer settings
2. 토큰 권한에 `repo` 포함 확인
3. 새 토큰 발급 후 .env 업데이트

### Q3: Hugging Face 다운로드 느림

**원인**: 토큰 없이 사용 중

**해결**:
```bash
# .env에 토큰 추가
HF_TOKEN=hf_your_token_here

# 또는 환경 변수로 설정
export HF_TOKEN=hf_your_token_here
```

### Q4: W&B 로그인 실패

**원인**: API 키가 잘못됨

**해결**:
```bash
# W&B 재인증
wandb login

# 또는 .env에서 키 확인
grep WANDB_API_KEY .env
```

---

## 🚀 사용 예시

### Python 코드에서 사용

```python
# 환경 변수 로드
from utils.env_loader import env, get_api_key, has_api_key

# API 키 가져오기
tavily_key = get_api_key('tavily')
if tavily_key:
    print("Tavily 사용 가능!")

# 키 존재 여부 확인
if has_api_key('github'):
    # GitHub 작업 수행
    from utils.env_loader import get_github_config
    config = get_github_config()
    print(f"GitHub 사용자: {config['username']}")

# 시스템 설정
from utils.env_loader import get_system_config
config = get_system_config()
print(f"최대 반복: {config['max_code_iterations']}회")
```

### 스크립트에서 사용

```bash
#!/bin/bash

# .env 로드
source .env

# API 키 사용
if [ -n "$TAVILY_API_KEY" ]; then
    echo "Tavily API 사용 가능"
    # 웹 검색 수행
fi
```

---

## 📚 추가 리소스

- **Tavily 문서**: https://docs.tavily.com
- **GitHub Token 가이드**: https://docs.github.com/en/authentication
- **Hugging Face 문서**: https://huggingface.co/docs
- **W&B 튜토리얼**: https://docs.wandb.ai

---

## ✅ 요약

1. **`.env.example`을 복사하여 `.env` 생성**
2. **필요한 API 키 발급 및 입력**
3. **`python check_env.py`로 확인**
4. **시스템 시작**: `claude code chat @supervisor`

**권장 설정 우선순위**:
1. 🥇 GitHub Token (repo 관리)
2. 🥈 Tavily API (웹 검색)
3. 🥉 Hugging Face Token (모델 다운로드)
4. 📊 W&B API Key (실험 추적)

API 키 없이도 시스템은 작동하지만, 일부 기능이 제한됩니다!

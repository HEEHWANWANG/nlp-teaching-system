"""
Environment Variable Loader
.env 파일을 로드하고 환경 변수를 관리하는 유틸리티
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any
import warnings


class EnvLoader:
    """환경 변수 로더 클래스"""
    
    def __init__(self, env_file: str = ".env"):
        """
        Args:
            env_file: .env 파일 경로 (기본값: ".env")
        """
        self.env_file = Path(env_file)
        self.variables: Dict[str, str] = {}
        
        if self.env_file.exists():
            self.load()
        else:
            warnings.warn(
                f"{env_file} 파일이 없습니다. "
                f".env.example을 복사하여 생성하세요: cp .env.example .env"
            )
    
    def load(self) -> None:
        """
        .env 파일을 읽어서 환경 변수로 설정
        """
        with open(self.env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # 주석이나 빈 줄 무시
                if not line or line.startswith('#'):
                    continue
                
                # KEY=VALUE 파싱
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # 따옴표 제거
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    
                    # 환경 변수 설정
                    os.environ[key] = value
                    self.variables[key] = value
        
        print(f"✅ 환경 변수 로드 완료: {len(self.variables)}개 변수")
    
    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        환경 변수 가져오기
        
        Args:
            key: 환경 변수 이름
            default: 기본값
        
        Returns:
            환경 변수 값 또는 기본값
        """
        return os.getenv(key, default)
    
    def get_required(self, key: str) -> str:
        """
        필수 환경 변수 가져오기 (없으면 에러)
        
        Args:
            key: 환경 변수 이름
        
        Returns:
            환경 변수 값
        
        Raises:
            ValueError: 환경 변수가 없을 때
        """
        value = self.get(key)
        if value is None or value == "":
            raise ValueError(
                f"필수 환경 변수 '{key}'가 설정되지 않았습니다. "
                f".env 파일을 확인하세요."
            )
        return value
    
    def get_bool(self, key: str, default: bool = False) -> bool:
        """
        불리언 환경 변수 가져오기
        
        Args:
            key: 환경 변수 이름
            default: 기본값
        
        Returns:
            불리언 값
        """
        value = self.get(key, str(default))
        return value.lower() in ('true', '1', 'yes', 'on')
    
    def get_int(self, key: str, default: int = 0) -> int:
        """
        정수 환경 변수 가져오기
        
        Args:
            key: 환경 변수 이름
            default: 기본값
        
        Returns:
            정수 값
        """
        value = self.get(key, str(default))
        try:
            return int(value)
        except ValueError:
            warnings.warn(f"'{key}' 값을 정수로 변환할 수 없습니다. 기본값 {default} 사용")
            return default
    
    def check_required_keys(self, keys: list[str]) -> Dict[str, bool]:
        """
        필수 키들이 설정되어 있는지 확인
        
        Args:
            keys: 확인할 키 리스트
        
        Returns:
            {key: is_set} 딕셔너리
        """
        results = {}
        for key in keys:
            value = self.get(key)
            results[key] = value is not None and value != ""
        return results
    
    def print_status(self) -> None:
        """
        현재 환경 변수 설정 상태 출력
        """
        print("\n" + "="*50)
        print("🔧 환경 변수 설정 상태")
        print("="*50)
        
        # API Keys
        print("\n📡 External API Keys:")
        api_keys = ['TAVILY_API_KEY', 'OPENAI_API_KEY', 'ANTHROPIC_API_KEY']
        for key in api_keys:
            status = "✅ 설정됨" if self.get(key) else "❌ 미설정"
            print(f"  {key:25s}: {status}")
        
        # GitHub
        print("\n🐙 GitHub:")
        github_keys = ['GITHUB_TOKEN', 'GITHUB_USERNAME', 'GITHUB_EMAIL']
        for key in github_keys:
            status = "✅ 설정됨" if self.get(key) else "❌ 미설정"
            print(f"  {key:25s}: {status}")
        
        # Hugging Face
        print("\n🤗 Hugging Face:")
        hf_keys = ['HF_TOKEN', 'HF_HOME']
        for key in hf_keys:
            value = self.get(key)
            status = "✅ 설정됨" if value else "❌ 미설정"
            print(f"  {key:25s}: {status}")
        
        # Experiment Tracking
        print("\n📊 Experiment Tracking:")
        exp_keys = ['WANDB_API_KEY', 'WANDB_PROJECT']
        for key in exp_keys:
            status = "✅ 설정됨" if self.get(key) else "❌ 미설정"
            print(f"  {key:25s}: {status}")
        
        # System Config
        print("\n⚙️ System Configuration:")
        sys_keys = ['MAX_CODE_ITERATIONS', 'TASK_TIMEOUT', 'LOG_LEVEL']
        for key in sys_keys:
            value = self.get(key, "기본값 사용")
            print(f"  {key:25s}: {value}")
        
        print("\n" + "="*50 + "\n")


# 전역 로더 인스턴스
env = EnvLoader()


# 편의 함수들
def get_api_key(service: str) -> Optional[str]:
    """
    API 키 가져오기
    
    Args:
        service: 'tavily', 'openai', 'anthropic', 'github', 'huggingface', 'wandb'
    
    Returns:
        API 키 또는 None
    """
    key_map = {
        'tavily': 'TAVILY_API_KEY',
        'openai': 'OPENAI_API_KEY',
        'anthropic': 'ANTHROPIC_API_KEY',
        'github': 'GITHUB_TOKEN',
        'huggingface': 'HF_TOKEN',
        'wandb': 'WANDB_API_KEY',
    }
    
    key_name = key_map.get(service.lower())
    if key_name is None:
        warnings.warn(f"알 수 없는 서비스: {service}")
        return None
    
    api_key = env.get(key_name)
    if not api_key:
        warnings.warn(
            f"{service} API 키가 설정되지 않았습니다. "
            f".env 파일에 {key_name}을 추가하세요."
        )
    return api_key


def has_api_key(service: str) -> bool:
    """
    API 키가 설정되어 있는지 확인
    
    Args:
        service: 서비스 이름
    
    Returns:
        설정 여부
    """
    api_key = get_api_key(service)
    return api_key is not None and api_key != ""


def get_github_config() -> Dict[str, Optional[str]]:
    """
    GitHub 설정 가져오기
    
    Returns:
        {'token': ..., 'username': ..., 'email': ...}
    """
    return {
        'token': env.get('GITHUB_TOKEN'),
        'username': env.get('GITHUB_USERNAME'),
        'email': env.get('GITHUB_EMAIL'),
    }


def get_wandb_config() -> Dict[str, Optional[str]]:
    """
    W&B 설정 가져오기
    
    Returns:
        {'api_key': ..., 'project': ..., 'entity': ...}
    """
    return {
        'api_key': env.get('WANDB_API_KEY'),
        'project': env.get('WANDB_PROJECT', 'nlp-teaching-project'),
        'entity': env.get('WANDB_ENTITY'),
    }


def get_system_config() -> Dict[str, Any]:
    """
    시스템 설정 가져오기
    
    Returns:
        시스템 설정 딕셔너리
    """
    return {
        'workspace_dir': env.get('WORKSPACE_DIR', './.claude/workspace'),
        'max_parallel_tasks': env.get_int('MAX_PARALLEL_TASKS', 3),
        'max_code_iterations': env.get_int('MAX_CODE_ITERATIONS', 3),
        'task_timeout': env.get_int('TASK_TIMEOUT', 3600),
        'log_level': env.get('LOG_LEVEL', 'INFO'),
        'default_model': env.get('DEFAULT_MODEL', 'claude-sonnet-4.5'),
        'dev_mode': env.get_bool('DEV_MODE', False),
        'debug': env.get_bool('DEBUG', False),
    }


# 사용 예시
if __name__ == "__main__":
    # 환경 변수 로드
    env_loader = EnvLoader()
    
    # 상태 출력
    env_loader.print_status()
    
    # 개별 키 확인
    print("\n🔍 API 키 확인:")
    for service in ['tavily', 'github', 'huggingface', 'wandb']:
        has_key = has_api_key(service)
        status = "✅" if has_key else "❌"
        print(f"  {status} {service}")
    
    # 시스템 설정 확인
    print("\n⚙️ 시스템 설정:")
    config = get_system_config()
    for key, value in config.items():
        print(f"  {key}: {value}")

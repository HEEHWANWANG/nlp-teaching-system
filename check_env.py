#!/usr/bin/env python3
"""
환경 변수 설정 상태를 확인하는 스크립트
"""

import sys
from pathlib import Path

# utils 모듈을 import 경로에 추가
sys.path.insert(0, str(Path(__file__).parent))

from utils.env_loader import env, has_api_key, get_system_config


def main():
    """메인 함수"""
    
    print("\n" + "="*60)
    print("🔧 NLP Teaching System - 환경 변수 체크")
    print("="*60)
    
    # .env 파일 존재 확인
    env_file = Path(".env")
    if not env_file.exists():
        print("\n❌ .env 파일이 없습니다!")
        print("\n해결 방법:")
        print("  1. .env.example을 복사하세요: cp .env.example .env")
        print("  2. .env 파일을 열어서 API 키들을 입력하세요")
        print("  3. 다시 이 스크립트를 실행하세요: python check_env.py")
        return 1
    
    # 상태 출력
    env.print_status()
    
    # 권장 사항
    print("\n💡 권장 사항:")
    
    recommendations = []
    
    # Tavily (웹 검색)
    if not has_api_key('tavily'):
        recommendations.append(
            "  🔍 Tavily API: 웹 검색 기능을 위해 설정을 권장합니다\n"
            "     → https://tavily.com 에서 무료 API 키 발급"
        )
    
    # GitHub
    if not has_api_key('github'):
        recommendations.append(
            "  🐙 GitHub Token: 자동 repo 생성/관리를 위해 설정을 권장합니다\n"
            "     → Settings > Developer settings > Personal access tokens"
        )
    
    # Hugging Face
    if not has_api_key('huggingface'):
        recommendations.append(
            "  🤗 Hugging Face Token: 모델 다운로드 제한 회피를 위해 권장\n"
            "     → https://huggingface.co/settings/tokens"
        )
    
    # W&B
    if not has_api_key('wandb'):
        recommendations.append(
            "  📊 W&B API Key: 실험 추적을 위해 권장합니다\n"
            "     → https://wandb.ai/authorize"
        )
    
    if recommendations:
        for rec in recommendations:
            print(rec)
    else:
        print("  ✅ 모든 권장 API 키가 설정되었습니다!")
    
    # 시스템 설정 확인
    config = get_system_config()
    print("\n⚙️ 현재 시스템 설정:")
    print(f"  • Code Loop 최대 반복: {config['max_code_iterations']}회")
    print(f"  • 병렬 작업 수: {config['max_parallel_tasks']}개")
    print(f"  • 타임아웃: {config['task_timeout']}초")
    print(f"  • 로그 레벨: {config['log_level']}")
    
    # 최종 안내
    print("\n" + "="*60)
    print("✅ 환경 변수 체크 완료!")
    print("="*60)
    print("\n📚 다음 단계:")
    print("  1. API 키 설정이 필요하면 .env 파일을 수정하세요")
    print("  2. 시스템을 시작하세요: claude code chat @supervisor")
    print("  3. 또는 README.md를 참고하세요")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

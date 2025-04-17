import os
import sys

# 루트 디렉토리 (news_trend)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# client_info.py가 있는 곳을 sys.path에 추가
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# 서브 폴더들도 자동으로 추가
PIPELINE_PATH = os.path.join(ROOT_DIR, 'news_pipeline')
if PIPELINE_PATH not in sys.path:
    sys.path.append(PIPELINE_PATH)

DAGS_PATH = os.path.join(ROOT_DIR, 'dags')
if DAGS_PATH not in sys.path:
    sys.path.append(DAGS_PATH)

# Flask 설정 파일
from dotenv import load_dotenv
import os


# Project 폴더 경로 & load .env 파일 
CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
PROJ_ROOT_DIR = os.path.dirname(CONFIG_DIR)
load_dotenv(dotenv_path=os.path.join(PROJ_ROOT_DIR, '.env'))
loaded_secret_key = os.environ.get('SECRET_KEY') # 👈 이 시점에 키가 없으면 None이 할당됨

# instance 폴더 경로
INSTANCE_PATH = os.path.join(os.path.dirname(__file__), "..", "instance")
os.makedirs(INSTANCE_PATH, exist_ok=True) # 폴더가 없으면 생성

class Config:
    """환경 설정 (로컬 SQLite 기본값)"""
    # SQLite 데이터베이스 설정
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/reviews.db")
    
    # 세션 관리를 위한 비밀 키
    SECRET_KEY = loaded_secret_key
    
    # 디버그 모드 설정
    DEBUG = True


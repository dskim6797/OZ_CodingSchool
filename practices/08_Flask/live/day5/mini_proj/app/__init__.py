from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from .config import Config

# DB 연결 엔진을 생성
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
    connect_args={"check_same_thread": False}   # 스레드 옵션
)

# 세션(SessionLocal) 객체 (with scoped_session)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False)) # 여러 요청이 동시에 들어와도 세션 충돌을 방지함

# Base 클래스(declarative_base)
Base = declarative_base()

def create_app():
    # Flask 앱 생성 및 초기화
    app = Flask(__name__)
    
    # 설정 로드: Config 객체로부터 모든 설정을 app.config에 로드
    app.config.from_object(Config) 

    # 모델을 import & DB 테이블 생성
    from . import models
    with app.app_context():
        Base.metadata.create_all(bind=engine) 
    
    # 라우트 블루프린트 등록 (review_routes 불러와서 app.register_blueprint)
    from .routes.review_routes import review_bp
    app.register_blueprint(review_bp)
    
    # 요청이 끝날 때마다 세션 닫기
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app



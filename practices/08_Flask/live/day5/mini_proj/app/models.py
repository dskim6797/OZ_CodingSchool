from sqlalchemy import Column, Integer, String, Text
from . import Base

# Review 모델 클래스 (Base 상속)
class Review(Base):
    __tablename__ = "reviews"

    # id, title, content, rating, created_at 컬럼 정의
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False) 
    rating = Column(Integer, nullable=False)  # 1~5점
    
    def __repr__(self):
        return f"<Review - '{self.title}'>"



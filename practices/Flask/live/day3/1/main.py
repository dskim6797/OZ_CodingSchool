from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# 데이터 베이스 연결
engine = create_engine("sqlite:///user.db", echo=True)

# Base 클래스 정의
Base = declarative_base()

# 모델(테이블) 정의
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    def __repr__(self): # 파이썬 객체를 개발자 친화적 문자로 표현
        return f"<User(id={self.id}, name='{self.name}')>"        

# DB 안에 테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 준비
SessionLocal = sessionmaker(bind=engine)

# ------ 단일 데이터 핸들링 ------ 
def run_single():
    db = SessionLocal()
    
    # Create (Insert)
    new_user = User(name="소민")
    db.add(new_user)
    db.commit()
    print("----------- 사용자 추가: ", new_user)

    # Read (Select)
    user = db.query(User).first()
    print("----------- 사용자 선택: ", user)

    # Update
    user = db.query(User).first()
    if user:
        user.name = "동석"
        db.commit()
        print("----------- 사용자 변경:", user)

    # Delete
    user = db.query(User).first()
    if user:
        db.delete(user)
        db.commit()
        print("----------- 사용자 삭제:", user)

    db.close()


# ------ 복수 데이터 핸들링 ------ 
db = SessionLocal()

# Create (Insert)
new_users = [User(name="소민"), User(name="BE_동석"), User(name="BE_건영")]
db.add_all(new_users)
db.commit()
print("----------- 사용자 추가: ", new_users)

# Read (Select)
### 전체 데이터 검색
users = db.query(User).all()
for user in users:
    print("----------- 전체 검색: ", user.name)
### 특정 데이터 검색
find_user = db.query(User).filter(User.name == "동석").first()
print("----------- 조건 검색: ", find_user)
### 패턴 검색
find_users = db.query(User).filter(User.name.like("BE_%")).all()
print("----------- 조건 검색: ", find_users)

# Update
users = db.query(User).all()
for user in users:
    user.name = user.name + "_new"
    db.commit()
print("----------- 사용자 변경:", users)
    
# Delete
user = db.query(User).delete()
db.commit()
users = db.query(User).all()
if users:
    print("----------- 남은 데이터", users)
else:
    print("----------- 빈 DB")

db.close()




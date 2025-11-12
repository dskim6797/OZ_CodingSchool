from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os

app = Flask(__name__)

##########
# DB 설정
##########
BASE_DIR = os.path.dirname(__file__)
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{os.path.join(INSTANCE_DIR, 'todos.db')}"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}   # 스레드 옵션
)

SessionLocal = sessionmaker(bind=engine)


##########
# 모델 정의
##########
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(200), nullable=False)

    def __repr__(self):
        return f"<Todo id={self.id} task='{self.task}'>"

Base.metadata.create_all(bind=engine)

##########
# CRUD API
##########

# Read: 전체 목록 조회
@app.route("/todos", methods=["GET"])
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id": t.id, "task": t.task} for t in todos])

# Read: 특정 목록 조회
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    db = SessionLocal()
    task = db.query(Todo).get(todo_id)
    db.close()
    if not task:
        return jsonify({"error": "그런건 없어요"}), 404
    return jsonify({todo_id: task})

# Create: 새로운 todo 추가
@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json() # body 값 받기

    db = SessionLocal()
    todo = Todo(task=data["task"])
    db.add(todo)
    db.commit()
    db.refresh(todo) # commit 이후로 자동 생성된 id 불러오기
    db.close()
    return jsonify({"id": todo.id, "task": todo.task}), 201

# Update: todo 수정
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json()

    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    # 데이터 없을 때
    if not todo:
        db.close()
        return jsonify({"error": "못찾았어요"}), 404

    # 데이터 있을 때
    todo.task = data["task"]
    db.commit()
    updated = {"id": todo.id, "task": todo.task}
    db.close()
    return jsonify(updated)

# Delete: todo 삭제
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({"error": "없어요"}), 404
    db.delete(todo)
    db.commit()
    db.close()
    return jsonify({"deleted": todo_id})

if __name__ == "__main__":
    app.run(debug=True)
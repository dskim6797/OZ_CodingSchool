from .models import SessionLocal, Todo
from flask import request, jsonify, Blueprint


todo_bp = Blueprint("todo", __name__)

##################################################
# CRUD API #######################################
##################################################

# Read: 전체 목록 조회
@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id": t.id, "task": t.task} for t in todos])

# Read: 특정 목록 조회
@todo_bp.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    db = SessionLocal()
    task = db.query(Todo).get(todo_id)
    db.close()
    if not task:
        return jsonify({"error": "그런건 없어요"}), 404
    return jsonify({todo_id: task})

# Create: 새로운 todo 추가
@todo_bp.route("/todos", methods=["POST"])
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
@todo_bp.route("/todos/<int:todo_id>", methods=["PUT"])
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
@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
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

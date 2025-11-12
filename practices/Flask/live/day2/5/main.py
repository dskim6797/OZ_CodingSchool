from flask import Flask, jsonify, request

app = Flask(__name__)

# 임시 데이터베이스
todos = {
    1: "밥먹기",
    2: "놀기"
}

# Read - 전체 목록 조회
@app.route("/todos", methods = ["GET"])
def get_todos():
    return jsonify(todos)
    
# Read - 특정 목록 조회
@app.route("/todos/<int:todo_id>", methods = ["GET"])
def get_todo(todo_id):
    task = todos.get(todo_id)
    if not task:
        return jsonify({"error": "Not found"}), 404
    return jsonify({todo_id: task})
    
# Create: 새로운 todo 추가
@app.route("/todos", methods = ["POST"])
def create_todo():
    data = request.get_json() # body 값 받기
    new_id = max(todos.keys()) + 1 if todos else 1
    todos[new_id] = data["task"]
    return jsonify({new_id: todos[new_id]}), 201

# Update: todo 수정
@app.route("/todos/<int:todo_id>", methods = ["PUT"])
def update_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "못찾았어요"}), 404
    data = request.get_json() # body 값 받기
    todos[todo_id] = data["task"]
    return jsonify({todo_id: todos[todo_id]})

# Delete: todo 삭제
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "없어요"}), 404
    deleted = todos.pop(todo_id)
    return jsonify({"deleted": deleted})


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request
from app.todo import TodoService

app = Flask(__name__)
todo_service = TodoService()


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/todos")
def get_todos():
    return jsonify(todo_service.list_items())

@app.get("/todos/<int:item_id>/")
def get_one_todo(item_id: int):
    try:
        item = todo_service.get(int(item_id))
        return jsonify(item)
    except KeyError:
        return jsonify({"error": "not found"}), 404

@app.post("/todos")
def add_todo():
    payload = request.get_json() or {}
    title = payload.get("title")
    try:
        item = todo_service.add(title)
        return jsonify(item), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.post("/todos/<int:item_id>/done")
def mark_done(item_id: int):
    try:
        item = todo_service.mark_done(int(item_id))
        return jsonify(item)
    except KeyError:
        return jsonify({"error": "not found"}), 404

@app.post("/todos/clear")
def clear_todos():
    todo_service.clear()
    if len(todo_service.list_items()) == 0:
        return jsonify({"message": "Todo list cleared successfully"})

    return jsonify({"message": "Unable to clear Todo list"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
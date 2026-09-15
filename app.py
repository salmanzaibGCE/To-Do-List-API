from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
tasks = []
task_id_counter = 1
 
@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks), 200
 
@app.route("/tasks", methods=["POST"])
def add_task():
    global task_id_counter
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400
    
    task = {
        "id": task_id_counter,
        "title": data["title"],
        "done": False
    }
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201
 
@app.route("/tasks/<int:task_id>/done", methods=["PUT"])
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task), 200
    return jsonify({"error": "task not found"}), 404
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
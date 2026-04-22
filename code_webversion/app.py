from flask import Flask, render_template, request, redirect, url_for

# Keep the current structure minimal by reusing files in this folder.
app = Flask(__name__, template_folder=".", static_folder=".")

todos = []
brain_dumps = []


@app.route("/")
def index():
    return render_template("index.html", todos=todos, brain_dumps=brain_dumps)


@app.route("/add", methods=["POST"])
def add():
    todo = (request.form.get("todo") or "").strip()
    if todo:
        todos.append(todo)
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    return redirect(url_for("index"))


@app.route("/brain_dump/add", methods=["POST"])
def add_brain_dump():
    note = (request.form.get("brain_dump") or "").strip()
    if note:
        brain_dumps.append(note)
    return redirect(url_for("index"))


@app.route("/brain_dump/delete/<int:note_id>", methods=["POST"])
def delete_brain_dump(note_id):
    if 0 <= note_id < len(brain_dumps):
        brain_dumps.pop(note_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
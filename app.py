from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from TodoController import TodoController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):  # how to extract it to another file??
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(100))
    status = db.Column(db.String(100))


@app.route("/")
def home():
    return TodoController.home(Todo)


@app.route("/add", methods=["POST"])
def add():
    return TodoController.add(Todo, db)


@app.route("/update/<int:todoId>", methods=["POST"])
def update(todoId):
    return TodoController.update(Todo, db, todoId)


@app.route("/delete/<int:todoId>")
def delete(todoId):
    return TodoController.delete(Todo, db, todoId)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

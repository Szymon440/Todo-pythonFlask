from flask import render_template, redirect, url_for
from TodoModel import TodoModel


class TodoController(object):
    def home(todo):
        return render_template("index.html", todoList=TodoModel.getAllTodo(todo))

    def add(todo, db):
        TodoModel.InsertDataToDatabase(todo, db)
        return redirect(url_for("home"))

    def update(todo, db, id):
        todoTakenById = TodoModel.getTodoById(todo, id)
        TodoModel.updateTodoStatus(todoTakenById, db)
        return redirect(url_for("home"))

    def delete(todo, db, id):
        todoTakenById = TodoModel.getTodoById(todo, id)
        TodoModel.deleteTodoById(todoTakenById, db)
        return redirect(url_for("home"))

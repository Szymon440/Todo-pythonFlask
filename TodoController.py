from flask import render_template, redirect, url_for
from TodoModel import TodoModel

class TodoController(object):
    def home(Todo):
        return render_template("index.html" , todoList=TodoModel.getAllTodo(Todo))

    def add(Todo, db):
        TodoModel.InsertDataToDatabase(Todo,db)
        return redirect(url_for("home"))

    def update(Todo , db, id):
        todo = TodoModel.getTodoById(Todo, id)
        TodoModel.updateTodoStatus(todo , db)
        return redirect(url_for("home"))

    def delete(Todo , db, id):
        todo = TodoModel.getTodoById(Todo, id)
        TodoModel.deleteTodoById(todo , db)
        return redirect(url_for("home"))

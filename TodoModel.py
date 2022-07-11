from flask import request


class TodoModel(object):
    def InsertDataToDatabase(todo, db):
        db.session.add(todo(taskName=request.form.get("taskName"), status=request.form.get("status")))
        db.session.commit()

    def getTodoById(todo, id):
        return todo.query.filter_by(id=id).first()

    def updateTodoStatus(todo, db):
        todo.status = request.form.get("updatedStatus")
        db.session.commit()

    def deleteTodoById(todo, db):
        db.session.delete(todo)
        db.session.commit()

    def getAllTodo(todo):
        return todo.query.all()

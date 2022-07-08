from flask import request

class TodoModel(object):#i think its can be better named
    def InsertDataToDatabase(Todo,db):
        db.session.add(Todo(taskName=request.form.get("taskName"),status=request.form.get("status")))
        db.session.commit()

    def getTodoById(Todo, id):
        return Todo.query.filter_by(id=id).first()

    def updateTodoStatus(todo, db):
        todo.status = request.form.get("updatedStatus")
        db.session.commit()

    def deleteTodoById(todo, db):
        db.session.delete(todo)
        db.session.commit()
        
    def getAllTodo(Todo):
        return Todo.query.all()
from flask import render_template, request, redirect
from config import db
from models.taskModel import Tasks
from models.authModel import Users


def index():
    tasks = Tasks.query.all()
    users = Users.query.all()
    return render_template('task.html', title= 'Home Page', tasks = tasks, users = users)



def add_task(): 
     return render_template('add-task.html', title='Add New Task')


def create():
     form = request.form
     title = form['title']
     description = form['description']
     leader = form['leader']

     tasks = Tasks(title=title, description=description, leader=leader)
     db.session.add(tasks)
     db.session.commit()

     return redirect('/')


def view(id):
     tasks = Tasks.query.get(id)

     return render_template('view.html',title='Details Page', tasks=tasks)



def update(id):
      tasks = Tasks.query.filter_by(id = id).first()
      if tasks is None:
           return redirect('/')
      if request.method == 'GET':
           return render_template('update.html',tasks=tasks)
      elif request.method == 'POST':
          form = request.form
          title = form['title']
          description = form['description']
          leader = form['leader']

          tasks.title= title
          tasks.description = description
          tasks.leader = leader

          db.session.commit() 
          return redirect('/')
      return render_template('update.html', title= 'Edit Task', tasks=tasks) 



def delete(id):
     if request.method == 'POST' :
          if request.form['_method'] == 'DELETE':
               article = Tasks.query.get(id)
               db.session.delete(article)
               db.session.commit()
               return redirect('/')

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Task
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template("welcome.html", user=current_user)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        task = request.form.get('task')#Gets the task from the HTML 

        if len(task) < 1:
            flash('Task is too short!', category='error') 
        else:
            new_note = Task(data=task, user_id=current_user.id)  #providing the schema for the task 
            db.session.add(new_note) #adding the task to the database 
            db.session.commit()
            flash('Task added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-task', methods=['POST'])
def delete_note():  
    task = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = task['noteId']
    task = Task.query.get(noteId)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()

    return jsonify({})

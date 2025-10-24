from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User, Task
from .forms import TaskForm, RegistrationForm, LoginForm

main = Blueprint('main', __name__)

# Home / Task list
@main.route('/')
@login_required
def home():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    form = TaskForm()
    return render_template('index.html', tasks=tasks, form=form)

# Add new task
@main.route('/add', methods=['POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash("Task added!", "success")
    else:
        flash("Invalid task title.", "danger")
    return redirect(url_for('main.home'))

# Toggle completion
@main.route('/complete/<int:task_id>')
@login_required
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id == current_user.id:
        task.complete = not task.complete
        db.session.commit()
    return redirect(url_for('main.home'))

# Delete task
@main.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('main.home'))

# Register
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing = User.query.filter_by(username=form.username.data).first()
        if existing:
            flash("Username already exists.", "danger")
            return redirect(url_for('main.register'))
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

# Login
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for('main.home'))
        else:
            flash("Invalid username or password.", "danger")
    return render_template('login.html', form=form)

# Logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for('main.login'))

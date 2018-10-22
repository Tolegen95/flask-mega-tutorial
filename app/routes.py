from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not user.check_password(password=form.password.data):
            flash('Incorrect user or login')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=form.remember_me.data)
            next_url = request.args.get('next')
            if not next_url or url_parse(next_url).netloc != '':
                next_url = url_for('index')
            return redirect(next_url)
    return render_template('login.html', title='Sign in', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You successfully registered')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@login_required
def index():
    return render_template('index.html', title='Main page')
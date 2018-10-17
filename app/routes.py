from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Success. Username = {username}, remember_me={remember_me}'.format(
            username=form.username.data,
            remember_me=form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/')
def index():
    return render_template('index.html', title='Main page')
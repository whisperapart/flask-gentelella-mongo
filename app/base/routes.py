from bcrypt import checkpw, hashpw, gensalt
from flask import jsonify, render_template, redirect, request, url_for, json
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import login_manager, mongoc
from app.base import blueprint
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import LoginUser


@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/<template>')
def route_template(template):
    return render_template(template + '.html')


@blueprint.route('/fixed_<template>')
@login_required
def route_fixed_template(template):
    return render_template('fixed/fixed_{}.html'.format(template))


@blueprint.route('/page_<error>')
def route_errors(error):
    return render_template('errors/page_{}.html'.format(error))


# Login & Registration
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = mongoc.db.user_info.find_one({"username": username}, {"_id": 0})
        if user and checkpw(password.encode('utf8'), user['password']):
            user_obj = LoginUser(username=user['username'])
            login_user(user_obj)
            return redirect(url_for('base_blueprint.route_default'))
        return render_template('errors/page_403.html')
    if not current_user.is_authenticated:
        return render_template(
            'login/login.html',
            login_form=login_form,
            create_account_form=create_account_form
        )
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/create_user', methods=['POST'])
def create_user():
    user = dict()
    user['username'] = request.form['username']
    udb = mongoc.db.user_info.find_one({"username": user['username'] }, {"_id": 0})
    if udb:
        return jsonify('duplicate')
    user['password'] = hashpw(request.form['password'].encode('utf8'), gensalt())
    mongoc.db.user_info.insert_one(user)
    return jsonify('success')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'


## Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from app.forms import AuthForm
from app.auth import auth
from app.firestore_service import get_user, put_user
from app.models import UserData, UserModel


@auth.route('/login', methods=['GET', 'POST'])
def login() -> render_template:
    login_form = AuthForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user_doc = get_user(username)

        if user_doc.to_dict():
            password_from_db = user_doc.to_dict()['password']
            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)
                login_user(user)
                flash('Bienvenido de nuevo!')
                redirect(url_for('hello'))
            else:
                flash("la información no coincide")
        else:
            flash("El usuario no existe")

        return redirect(url_for('index'))

    return render_template('login.html', **context)


@auth.route('logout')
@login_required
def logout() -> redirect:
    logout_user()
    flash("Regresa pronto")
    return redirect(url_for("auth.login"))


@auth.route('signup', methods=['GET', 'POST'])
def signup() -> render_template:
    signup_form = AuthForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)
        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username=username, password=password_hash)
            put_user(user_data)
            user = UserModel(user_data)
            login_user(user)
            flash("Bienvenido")
            return redirect(url_for('hello'))
        else:
            flash("El usuario ya existe!")
    return render_template('signup.html', **context)

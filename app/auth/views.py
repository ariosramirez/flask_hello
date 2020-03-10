from flask import render_template
from app.forms import LoginForm

from app.auth import auth

@auth.route('/login')
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render_template('login.html', **context)


from flask import (Flask,
                   request,
                   make_response,
                   redirect,
                   render_template,
                   session)
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SUPER SECRETO'


to_do_list = ['Comprar café', 'ir a el banco', 'Compar fruta']


class LoginFrom(FlaskForm):
    user_name = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(500)
def not_found_500(error):
    return render_template('500.html', error=error)

@app.errorhandler(404)
def not_found_404(error):
    return render_template('404.html', error=error)



@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response((redirect('/hello')))
    session['user_ip'] = user_ip
    return response


@app.route('/hello')
def hello_world():
    user_ip = session.get('user_ip')
    login_form = LoginFrom()
    context = dict(user_ip=user_ip,
                   todos=to_do_list,
                   login_form=login_form)
    return render_template('hello.html', **context)


@app.route('/500_error_test')
def index_pandas():
    500


if __name__ == '__main__':
    app.run()


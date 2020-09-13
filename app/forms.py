from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class AuthForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Create')


class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Delete')


class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Update')

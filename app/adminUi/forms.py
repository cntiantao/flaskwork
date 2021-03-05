from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, MultipleFileField
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileStorage
from wtforms.validators import ValidationError


class LoginForm(FlaskForm):
    username = StringField('username', [validators.DataRequired(), validators.length(min=6)])
    password = PasswordField('password', [validators.DataRequired(), validators.length(min=6)])
    smtLogin = SubmitField('登陆')

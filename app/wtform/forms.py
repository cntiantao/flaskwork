from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    # username = StringField('username', render_kw={'placeholder':'用户名'},validators=[DataRequired()])
    username = StringField('username', render_kw={'placeholder': '用户名'})
    password = PasswordField('password')
    remember = BooleanField('rememberme')
    submit = SubmitField('Login')

from flask import render_template, flash, redirect, url_for, request
from app.wtform import wtform
from app.wtform.forms import LoginForm


@wtform.route('/wtform/index', methods=['GET', 'POST'])
def wtform_index():
    loginForm = LoginForm()
    if request.method == 'POST' and loginForm.validate():
        username = request.query_string
        print(username)
        return redirect(url_for('wtform.wtform_index'))
    return render_template('/wtform/home.html', loginForm=loginForm)

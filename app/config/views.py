from flask import render_template, redirect, url_for, abort, make_response, jsonify
from flask import current_app, request

from app.config import config
from app.manage import app
from app.config.function import func,redirect_back


@config.route('/config')
@config.route('/config/')
def config_index():
    # print(current_app)
    return '这是config模块首页\n path-->/config/'


@config.route('/config/show/<configName>', methods=['GET', 'POST'])
def show_config(configName):
    CONFIGNAME = str.upper(configName)
    return app.config[CONFIGNAME]


@config.route('/config/test/<arg>')
def test_func(arg):
    return app.config[str.upper(arg)]


@config.route('/config/redirect')
def config_redirect():
    return redirect('https://www.baidu.com')


@config.route('/config/redirect2')
def config_redirect2():
    # url_for()函数参数格式如下
    return redirect(url_for('config.config_referrer', next=request.full_path))


@config.route('/config/base')
def config_templates_base():
    return render_template('/config/base.html', config=app.config)


@config.route('/config/index')
def config_templates_index():
    return render_template('/config/home.html', config=app.config)


@config.route('/config/detail')
def config_templates_detail():
    return render_template('/config/detail.html', config=app.config)


@config.route('/config/showDog')
def config_show_gog():
    return render_template('/config/showDog.html', config=app.config)


@config.route('/config/abort')
def config_abort():
    # abort() 函数不用return ，但abort()函数后面的代码不会执行
    abort(404)


@config.route('/config/response')
def config_response():
    # response = make_response('这是response返回类型的测试')
    # response.mimetype = 'text/plain'
    # response.mimetype = 'text/html'
    # response.mimetype = 'application/xml'
    # response.mimetype = 'application/json'
    # return response
    return jsonify(name='Grey Li', gender='male')


@config.route('/config/referrer')
def config_referrer():
    # request.referrer 属性，记录了当前请求的上一个请求来源
    print('请求来源：', request.referrer)
    return redirect_back()











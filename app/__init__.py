from flask import Flask
from app.configuration import configuration


def create_app(config_name):
    # 初始化
    app = Flask(__name__)

    # 导致指定的配置对象:创建app时，传入环境的名称
    app.config.from_object(configuration[config_name])

    # 注册所有蓝本
    regist_blueprints(app)

    return app


def regist_blueprints(app):
    # 导入蓝本对象 并 注册config蓝本
    from app.config import config as config_blueprint
    app.register_blueprint(config_blueprint)


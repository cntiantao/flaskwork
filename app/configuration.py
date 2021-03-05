import os


# 配置环境的基类
class BaseConfig(object):
    # 每次请求结束后，自动提交数据库中的变动，该字段在flask-sqlalchemy 2.0之后已经被删除了（有bug）
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 2.0之后新加字段，flask-sqlalchemy 将会追踪对象的修改并且发送信号。
    # 这需要额外的内存，如果不必要的可以禁用它。
    # 注意，如果不手动赋值，可能在服务器控制台出现警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 数据库操作时是否显示原始SQL语句，一般都是打开的，因为后台要日志
    SQLALCHEMY_ECHO = True


# 开发环境的配置
class DevelopmentConfig(BaseConfig):
    """
    配置文件中的所有的账号密码等敏感信息，应该避免出现在代码中，可以采用从环境变量中引用的方式，比如：
    username = os.environ.get('MYSQL_USER_NAME')
    password = os.environ.get('MYSQL_USER_PASSWORD')
    本文为了便于理解，将用户信息直接写入了代码里
    """

    DEBUG = True
    ENV = 'development'
    # 数据库URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/lecar'

    # 也可如下来写，比较清晰
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(username="xxxx", password="123456", hostname="172.17.180.2", databasename="cleven_development")

    # SECRET_KEY标识session用于加密cookie的密钥， 存于.env环境变量中，如果获取失败，赋予默认值：123456
    SECRET_KEY = os.getenv('SECRET_KEY', '123456')

    # 表示cookie的有效期
    PERMANENT_SESSION_LIFETIME = 7

    # wtform是否开启 CSRF 验证保护的开关，默认为True
    WTF_CSRF_ENABLED = True

    # 上传文件时，默认可以接受的文件后缀类型
    ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']


# 测试环境的配置
class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@172.17.180.3:3306/cleven_test'

    """
    测试环境也可以使用sqlite，默认指定为一个内存中的数据库，因为测试运行结束后无需保留任何数据
    也可使用  'sqlite://' + os.path.join(basedir, 'data.sqlite') ，指定完整默认数据库路径
    """
    # import os
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


# 生产环境的配置
class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@172.17.180.4:3306/cleven_production'


# 初始化app实例时对应的开发环境声明
configuration = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

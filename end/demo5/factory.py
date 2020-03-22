# Charlie
# date:2020/3/16 17:54
# file_name:factory

"""
Flask - 应用工厂
"""
from werkzeug.utils import redirect
# 1.引入Flask
from flask import Flask, request, render_template, flash
from views import *
from models import *


# 2.构建Flask对象，就是一个WSGI应用 __name__为losk寻找static以及templates提供支持
def create_app():
    app = Flask(__name__)

    app.secret_key = '\x894<G\x92\x12\xe1e\xd7\xfa-R*\x147Nz\xbf\xcbc\xb0e6\xc1'
    # app.config['MATL_SERVER'] = 'smtp.qq.com'
    # # app.config['MATL_PORT'] = 25
    # app.config['MATL_USERNAME'] = 'r15290118724@163.com'
    # app.config['MATL_PASSWORD'] = 'LHUBFTRDPCLGDUIU'
    # app.config['MATL_DEFAULT_SENDER'] = '注册账号激活<335176033@qq.com>'

    app.config["MAIL_SERVER"] = "smtp.qq.com"
    app.config["MAIL_PORT"] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config["MAIL_USERNAME"] = "335176033@qq.com"
    app.config["MAIL_PASSWORD"] = "ngquotzkqgsnbggj"
    app.config['MAIL_DEFAULT_SENDER'] = '激活账号<335176033@qq.com>'

    app.register_blueprint(bookbp)
    app.register_blueprint(userbp)
    app.register_blueprint(adminbp)
    # 扩展工厂  关联邮件
    mail.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo5.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app

    @app.template_filter()
    def myupperfun(value):
        return value.capitalize()

    # @app.before_first_request
    # def first_request_do_something():

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    return app

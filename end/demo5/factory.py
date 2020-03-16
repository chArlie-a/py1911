# Charlie
# date:2020/3/16 17:54
# file_name:factory

"""
Flask - 应用工厂
"""
from werkzeug.utils import redirect
# 1.引入Flask
from flask import Flask, request, render_template, flash


# 2.构建Flask对象，就是一个WSGI应用 __name__为losk寻找static以及templates提供支持
def create_app():
    app = Flask(__name__)

    app.secret_key = '\x894<G\x92\x12\xe1e\xd7\xfa-R*\x147Nz\xbf\xcbc\xb0e6\xc1'

    @app.route('/')
    def index():
        bookList = [
            {
                'ID': 101,
                "NAME": "神雕侠侣"
            },
            {
                'ID': 102,
                "NAME": "天龙八部"
            },
            {
                'ID': 103,
                "NAME": "鹿鼎记"
            },
            {
                'ID': 104,
                "NAME": "笑傲江湖"
            }
        ]
        user = [
            {
                'Name': 'charlie'
            }
        ]
        return render_template('index.html', bl=bookList, u=user)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            # 7.使用render_template渲染jinja2模板
            # 模板文件和python模块同级
            # 8.静态资源static用法等同template
            return render_template('login.html')
        elif request.method == 'POST':
            # 6.从form中提取参数
            username = request.form.get('username')
            password = request.form.get('password')
            error = None
            if not username:
                error = "用户名必填"
            if not password:
                error = "密码必填"
            # 需要在本次请求中将信息写入session （前提必须配置secret_key）
            # flash("提示内容")
            # 下次请求中取获取、并且从session移除
            # get_flashed_messages()
            if error:
                flash(error, category=error)
                return redirect('/')
            return render_template('login.html', booklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username=username)

    @app.route('/regist', methods=['GET', 'POST'])
    def regist():
        if request.method == 'GET':
            return render_template('regist.html')
        elif request.method == 'POST':
            username = request.form.get("username")
            password = request.form.get("password")
            password2 = request.form.get("password2")
            error = None
            if not username:
                error = '用户名不能为空'
            elif not password:
                error = '密码不能为空'
            elif not password2:
                error = '重复密码不能为空'
            elif password != password2:
                error = '密码不一致'
            if error:
                flash(error, category=error)
                return redirect('/regist')
            return redirect('/')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    return app

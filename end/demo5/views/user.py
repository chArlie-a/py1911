# Charlie
# date:2020/3/16 17:49
# file_name:user
from flask import Blueprint, render_template, request, flash, current_app, make_response,session
from werkzeug.utils import redirect
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature
from datetime import timedelta, datetime
from models import *
userbp = Blueprint('user', __name__)


@userbp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 7.使用render_template渲染jinja2模板
        # 模板文件和python模块同级
        # 8.静态资源static用法等同template
        return render_template('login.html')
    elif request.method == 'POST':
        # 6.从form中提取参数
        email = request.form.get('username')
        password = request.form.get('password')
        error = None
        if not email:
            error = "用户名必填"
        if not password:
            error = "密码必填"
        # 需要在本次请求中将信息写入session （前提必须配置secret_key）
        # flash("提示内容")
        # 下次请求中取获取、并且从session移除
        # get_flashed_messages()
        if error:
            flash(error, category="error")
            return redirect('/login')
        else:
            with sqlite3.connect('demo5.db') as con:
                cur = con.cursor()
                cur.execute('select * from user where email = ?', (email,))
                r = cur.fetchall()
                if len(r) <= 0:
                    flash('用户名错误')
                    return redirect('/login')
                else:
                    securityPassword = r[0][2]
                    if not check_password_hash(securityPassword, password):
                        flash('密码错误')
                        return redirect('/login')
                    else:
                        if r[0][5] == 0:
                            flash('用户未激活不能登录')
                            return redirect('/login')
                        else:
                            next = request.args.get('next')
                            if next:
                                res = make_response(redirect(next))
                                # res.set_cookies('user', email, expires=datetime.now() + timedelta(days=7))
                                session['user'] = email
                                return res
                            else:
                                res = make_response(redirect('/'))
                                # res.set_cookies('user', email, expires=datetime.now() + timedelta(days=7))
                                session['user'] = email
                                return res
        # return render_template('login.html', booklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username=username)


@userbp.route('/logout')
def logout():
    res = make_response(redirect('/'))
    # res.delete_cookie('user')
    session.pop('user')
    return res


@userbp.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    elif request.method == 'POST':
        email = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        error = None
        if not email:
            error = '用户名不能为空'
        elif not password:
            error = '密码不能为空'
        elif not password2:
            error = '重复密码不能为空'
        elif password != password2:
            error = '密码不一致'
        if error:
            flash(error, category="error")
            return redirect('/regist')
        else:
            with sqlite3.connect('demo5.db') as con:
                cur = con.cursor()
                cur.execute('select * from user where email = ?', (email,))
                r = cur.fetchall()
                print(r)
                if len(r) > 0:
                    flash('用户已存在')
                    return redirect('/regist')
                else:
                    try:
                        from flask_mail import Message
                        from .utils import mail
                        security_password = generate_password_hash(password)
                        cur.execute('insert into user (email,password) values (?,?)', (email, security_password))
                        cur.execute('select id from user where email = ?', (email,))
                        id = cur.fetchone()[0]
                        print(id, '这是邮箱')

                        serUtil = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=24 * 60 * 60)
                        serstr = serUtil.dumps({'id': id}).decode('utf-8')

                        from tasks import sendmail
                        sendmail.delay((email, serstr))
                        con.commit()
                        return '注册成功'
                    except Exception as e:
                        print(e)
                        return '出异常了'


@userbp.route('/active/<id>')
def activeuser(id):
    try:
        serUtil = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=24 * 60 * 60)
        id = serUtil.loads(id)['id']
        with sqlite3.connect('demo5.db') as con:
            cur = con.cursor()
            cur.execute('update user set is_active = 1 where id = ?', (id,))
            con.commit()
        return redirect('/login')
    except SignatureExpired:
        return '超时了'
    except BadSignature:
        return '密钥错误'
    except Exception:
        return '未知原因导致激活失败'




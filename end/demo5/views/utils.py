# Charlie
# date:2020/3/17 17:23
# file_name:utils
"""
视图工具模块
"""
# 扩展Flask模块  定义邮件模块
from flask_mail import Mail
from flask import session, redirect, request
from functools import wraps

mail = Mail()


# 定义检测是否有用户登录得装饰器
def checklogin(f):
    @wraps(f)
    def check(*args, **kwargs):
        user = session.get('user')
        if user:
            return f(*args, **kwargs)
        else:
            return redirect('/login?next=' + request.path)

    return check

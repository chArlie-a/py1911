# Charlie
# date:2020/3/18 14:26
# file_name:tasks
"""
pip install celery 安装celery
安装redis数据库
pip install redis 安装python 处理redis数据库互动
"""
import time
from celery import Celery
from flask import current_app

app = Celery('tasks', broker='redis://127.0.0.1:6379/10', brckend='redis://127.0.0.1:6379/11')


# 构建任务
@app.task()
def dosomething():
    print('开始执行')
    time.sleep(5)
    print('执行结束')
    return 1000


from flask_mail import Message
from views import mail


@app.task()
def sendmail(email, serstr):
    with current_app.app_context():
        msg = Message(subject='老张大讲堂', recipients=[email])
        msg.html = "<a href='http://127.0.0.1:5000/active/%s'> 点击激活 </a> " % (serstr,)
        mail.send(msg)

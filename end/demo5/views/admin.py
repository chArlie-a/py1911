# Charlie
# date:2020/3/19 15:42
# file_name:admin
from flask import session, render_template, Blueprint, request
from werkzeug.utils import redirect
from models import *
from .utils import checklogin

adminbp = Blueprint('admin', __name__)


@adminbp.route('/admin')
@checklogin
def admin():
    """
    查看用户是否登录
    如果登录了则跳转admin页面
    如果没有登录则去登陆页面  登录之后再进入admin
    :return:
    """

    cs = Category.query.all()
    bs = Book.query.all()
    return render_template('admin/admin.html', cs=cs, bs=bs)


@adminbp.route('/admin/<resourcetype>/add', methods=['GET', 'POST'])
@checklogin
def add(resourcetype):
    resourcetype = resourcetype.capitalize()
    resource = globals()[resourcetype]
    if request.method == 'GET':
        fields = []
        ps = dir(resource)
        for p in ps:
            if (not p.startswith('__')) and (not p.startswith('_')) and (
                    p not in ['metadata', 'query', 'query_class', 'id', 'books']):
                fields.append(p)
        return render_template('admin/add.html', fs=fields)
    else:
        c = resource()
        c.name = request.form['name']
        db.session.add(c)
        db.session.commit()
        return redirect('/admin')


@adminbp.route('/admin/<resourcetype>/delete/<id>')
@checklogin
def delete(resourcetype, id):
    resourcetype = resourcetype.capitalize()
    resource = globals()[resourcetype]
    c = resource.query.filter_by(id=id).first()
    db.session.delete(c)
    db.session.commit()
    return redirect('/admin')

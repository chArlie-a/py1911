# Charlie
# date:2020/3/16 17:49
# file_name:book
from flask import Blueprint, render_template
from models.book import *

bookbp = Blueprint('book', __name__)


@bookbp.route('/')
def index():
    cs = Category.query.all()
    return render_template('index.html', cs=cs)


@bookbp.route("/categorys/<id>")
def category(id):
    c = Category.query.filter_by(id=id).first()
    if c:
        # 表关联查询
        # bs = Book.query.filter_by(cid=c.id).all()
        # 关系字段查询
        bs = c.books
        print(bs[0].category.id, bs[0].category.name)
        return render_template('category.html', bs=bs)
    return '输入不合法'

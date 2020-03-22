# Charlie
# date:2020/3/17 10:57
# file_name:run2
from tasks import dosomething
from tasks import sendmail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer

# app = Flask(__name__)
# # 配置数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo5.db'
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)

#
# class Category(db.Model):
#     id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column('name', db.String(50), nullable=False, unique=True)
#
#     def __repr__(self):
#         return self.name


# if __name__ == '__main__':
# app.run()
# 创建数据库表 初始化 发生在第一次运行
# db.create_all()
# c1 = Category()
# c1.name = '汽车'
# db.session.add(c1)
# db.session.commit()
#
# c2 = Category()
# c2.name = '服饰'
# db.session.add(c2)
# db.session.commit()

# cs = Category.query.all()
# print(cs)

# c = Category.query.filter_by(name='汽车').first()
# c.name = '交通工具'
# db.session.commit()
# print(c)
# db.session.delete(c)
# db.session.commit()
# pass
# if __name__ == '__main__':
# dosomething()
# dosomething()
# dosomething()
# r1 = dosomething.delay()
# r2 = dosomething.delay()
# r3 = dosomething.delay()
# print('所有任务完工了')
# r3 = sendmail.delay()
# print(r3)

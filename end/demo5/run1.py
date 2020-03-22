# Charlie
# date:2020/3/16 9:44
# file_name:run1
from factory import create_app
from models.utils import db

if __name__ == '__main__':
    # 开发环境使用
    app = create_app()
    # db.drop_all()
    # db.create_all()
    app.run(debug=True)
#  SQLALChemy  很典型的PYTHON ORM框架神器

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from info import create_app, db
from info.models import User

app = create_app("development")

manage = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manage.add_command('db', MigrateCommand)


@manage.option('-n', '-name', dest='name')
@manage.option('-p', '-password', dest='password')
def createsuperuser(name, password):

    if not all([name, password]):
        print("参数不足")

    user = User()
    user.nick_name = name
    user.mobile = name
    user.password = password
    user.is_admin = True

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)

    print("添加成功")


if __name__ == '__main__':
    # print(app.url_map)
    # app.run()
    manage.run()
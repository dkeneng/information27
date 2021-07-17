from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from info import create_app, db

app = create_app("development")

manage = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # print(app.url_map)
    # app.run()
    manage.run()
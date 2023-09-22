import argparse

import sys
import os
sys.path.append(os.getcwd())

from migrate.versioning import api
from panax.database import Base

import config.db
from models import *


def init():
    print("==init==")
    print("==finished==")


def migrate():
    print("==migrateing==")

    Base.metadata.create_all()
    # repo = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db_migrate')
    repo = os.path.join(os.getcwd(), 'db_migrate')
    if not os.path.exists(repo):
        api.create(repo, 'database repository')
        api.version_control(config.db.conn, repo)

    migration = repo + '/versions/%03d_migration.py' % (api.db_version(config.db.conn, repo) + 1)
    old_model = api.create_model(config.db.conn, repo)
    import types

    new = types.ModuleType('old_model')
    exec(old_model, new.__dict__)
    script = api.make_update_script_for_model(config.db.conn, repo, new.meta, Base.metadata)
    # print(script)
    open(migration, 'wt').write(script)
    api.upgrade(config.db.conn, repo)

    print("==migrate finished==")


# def upgrade():
#     print("==upgrade==")
#     repo = os.path.join(os.getcwd(), 'db_migrate')
#     if not os.path.exists(repo):
#         print("Repo Not Found!")
#
#     api.upgrade(config.db.conn, repo)


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-f", help="")
    parser.add_argument("exec", help="参数: [init, migrate, upgrade]")

    # 解析
    args = parser.parse_args()
    exec = args.exec
    # f = args.f

    if exec == "init":
        init()
    elif exec == "migrate":
        migrate()
    # elif exec == "upgrade":
    #     upgrade()
    else:
        print("参数错误")


if __name__ == '__main__':
    main()

import argparse


def init():
    print("==init==")


def migrate():
    print("==migrate==")


def upgrade():
    print("==upgrade==")


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-f", help="")
    parser.add_argument("text", help="参数: [init, migrate, upgrade]")

    # 解析
    args = parser.parse_args()
    text = args.text
    # f = args.f

    if text == "init":
        init()
    elif text == "migrate":
        migrate()
    elif text == "upgrade":
        upgrade()
    else:
        print("参数错误")


if __name__ == '__main__':
    main()

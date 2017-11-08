import os


def clean():
    os.system("rm -rf __pycache__")
    os.system("rm .DS_Store")
    os.system("clear")


if __name__ == '__main__':
    clean()

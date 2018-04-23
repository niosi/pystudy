# coding=utf-8
from datetime import datetime, timedelta

if __name__ == '__main__':
    print(datetime.strftime(datetime.now(), "%Y-%m-%d"))
    print(datetime.strftime(datetime.now() + timedelta(days=1), "%Y-%m-%d"))

import pymysql
import json
from datetime import datetime, date

conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       passwd="root",
                       port=3306,
                       database="test",
                       charset="utf8")
curs = conn.cursor(cursor=pymysql.cursors.DictCursor)

curs.execute("SELECT * FROM stu_test")

values = curs.fetchall()


def __default(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)


for i in values:
    print(type(i), type(json.dumps(i, default=__default)))

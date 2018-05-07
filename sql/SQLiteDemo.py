import sqlite3

# 创建链接对象
conn = sqlite3.connect("sqlitedemo.db")

# 创建游标对象
curs = conn.cursor()

# 执行SQL脚本语句
# curs.execute("create table sqlitetest (id integer primary key autoincrement, name varchar(50))")

try:
    # 插入一条数据
    curs.execute("insert into sqlitetest (name) values ('zhang')")
    # 插入第二条数据
    curs.execute("insert into sqlitetest (name) values ('li')")
except sqlite3.IntegrityError as e:
    print(e)

# 查看是否已经正确插入一条数据
print(curs.rowcount)

# 查看已经存在的数据信息
curs.execute("select * from sqlitetest where id =?", ('2',))

values = curs.fetchall()

curs.execute("select * from v_sqlitetest")

values2 = curs.fetchall()

for i, k in values:
    print(i, '-', k)

for i2, k2 in values2:
    print(i2, '-', k2)

# 关闭游标
curs.close()

# 提交事务处理
conn.commit()

# 关闭链接

conn.close()

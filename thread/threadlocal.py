# coding=utf-8
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()
class Teacher(object):
    thid = "def"
    thname = "def"
    def __init__(self, thid, thname):
        self.thid = thid
        self.thname = thname

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    th = local_school.teacher
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    print('Hello, %s (in %s)' % (th.thid, threading.current_thread().name))


def process_thread(name,th):
    # 绑定ThreadLocal的student:
    local_school.student = name
    local_school.teacher = th
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice', Teacher("1121", "wls")), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', Teacher("0311", "lls")), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

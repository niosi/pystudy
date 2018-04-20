class User(object):
    uid = 0
    uname = ""
    _uage = 0

    def __init__(self, uid, uname, uage):
        self.uid = uid
        self.uname = uname
        self._uage = uage

    def GetUage(self):
        return self._uage

    def setUage(self, uage):
        self._uage = uage

    def printInfo(self):
        print(str(self.uid) + ":" + self.uname + ":" + str(self._uage))


class Student(User):
    sno = ""


if __name__ == '__main__':
    stu = Student(1, "1", 1)
    stu.printInfo()
    # stu.__setattr__("usex","Boy")
    # print(hasattr(stu,"usex"))
    print(stu.usex)

import contextlib


class QueryTest(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_val)
        else:
            print("End")

    def simpleprint(self):
        print(self.name)


q = QueryTest("zhang")
q.simpleprint()
with QueryTest("li") as qs:
   qs.simpleprint()

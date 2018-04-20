class People(object):
    def __init__(self, uname, uage):
        self.uname = uname
        self.uage = - uage

    def PrintScore(self, score):
        print("%s score is %d" % (self.uname, score))
        return score

    def PringRank(self, score):
        if score >= 90:
            print("A")
        elif score >= 60:
            print("B")
        else:
            print("C")


if __name__ == '__main__':
    people = People("ZS", 18)
    people2 = People("LS", 20)
    people.PringRank(people.PrintScore(80))
    people2.PringRank(people2.PrintScore(90))

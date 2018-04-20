if __name__ == '__main__':
    with open("test", "a+") as f2:
        f2.write('\nHello Python')

    f = open("test", "r")
    print(f.read())
    f.close()

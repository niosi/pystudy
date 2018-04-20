# coding=utf-8
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


if __name__ == '__main__':
    # 测试:
    # if trim('hello  ') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello  ') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello  world  ') != 'hello  world':
    #     print('测试失败!')
    # elif trim('') != '':
    #     print('测试失败!')
    # elif trim('    ') != '':
    #     print('测试失败!')
    # else:
    #     print('测试成功!')
    for n in fab(5):
        print (n)

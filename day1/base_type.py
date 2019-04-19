# 中午写三个方法，方法名字test1  ，test2  ,test3   每个方法打印自己方法名，然后在main方法里面调用执行顺序是312

# def test1():
# print('wer')
# def test2():
# print('rty')
# def test3():
# print('ghj')


# if __name__ == '__main__':
# test3()
# test1()
# test2()

'''def int_deom():
    aint = 5
    print(aint)
    print(type(aint))


if __name__ == '__main__':
    int_deom()
'''


def str_demo():
    astr = '1'
    print(astr)
    print(type(astr))

    # if __name__ == '__main__':


def float_dome():
    float = 1.2
    print(float)
    print(type(float))


# 加法方法演示
def add_dome(a, b):
    print(a + b)



def type_zhuanhuan():
    aint = 1
    print(type(aint))
    print(type(str(aint)))
    print(type(int(aint)))


# 字符串拼接
def str_join():
    a = 123
    b = 1.22
    c = '你好'
    print(str(a) + str(b) + c)
    print('%s %s %s ' % (a, b, c))


def jianfa_dome(a, b):
    c=a - b
    return c



if __name__ == '__main__':
    # float_dome()
    # add_dome(1, 3)
    # type_zhuanhuan()
    # str_join()
    c=jianfa_dome(8, 6)
    d=add_dome(1,2)
    print(c)
    print(d)


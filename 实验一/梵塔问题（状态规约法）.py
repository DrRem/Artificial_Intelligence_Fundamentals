# 梵塔问题
step = 1


def move(n, a, b):
    global step
    notice = '第' + str(step) + '步：' + '圆盘' + str(n) + '从' + a + '移动到' + b
    print(notice)
    step = step + 1


def vatican(n, a, b, c):
    if n == 1:
        move(n, a, c)
    else:
        vatican(n - 1, a, c, b)
        move(n, a, c)
        vatican(n - 1, b, a, c)


if __name__ == "__main__":
    vatican(3, 'a', 'b', 'c')

# 模拟遗传算法
import random
import difflib

target_data = ''
sample_space = []  # 样本空间
m = 0   # 用于交换监控
n = 0
p = 0


def init():  # 初始化
    global sample_space
    global target_data
    target_data = '{:032b}'.format(int(random.randint(0, int(pow(2, 32) - 1))))  # 初始化目标状态
    while not len(sample_space) >= 32:  # 初始化样本空间
        n = int(random.randint(0, int(pow(2, 32) - 1)))
        t = '{:032b}'.format(n)
        if t not in sample_space:
            sample_space.append(t)


def fitness(sample):  # 适应度评价
    return difflib.SequenceMatcher(None, sample, target_data).ratio()


def selection():
    fit = []
    sample_fit = []
    global sample_space
    for i in sample_space:      # 测算每个个体的适应率
        f = fitness(i)
        if f == 1:
            return i
        else:
            fit.append(f)

    fit.sort()

    for i in fit[0:16]:      # 选择适应性最好的16个
        for j in sample_space:  # 测算每个个体的适应率
            f = fitness(j)
            if f == i:
                if j not in sample_fit:
                    sample_fit.append(j)
                    break

    sample_space = sample_fit
    return False


def cross():
    global sample_space
    global m
    global n
    global p
    for i in range(0, 16):      # 两两随机交换十六次
        m = random.randint(0, 15)
        n = random.randint(0, 15)
        p = random.randint(1, 31)
        sample_space.append(sample_space[m][0:p] + sample_space[n][p-1:31])


if __name__ == '__main__':
    init()
    while not selection():
        cross()
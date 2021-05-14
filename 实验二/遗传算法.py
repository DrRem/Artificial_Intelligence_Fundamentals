# 模拟遗传算法
import random
import difflib

target_data = ''
sample_space = []  # 样本空间


def init():  # 初始化
    global sample_space
    global target_data
    target_data = '{:032b}'.format(random.randint(0, pow(2, 32) - 1))  # 初始化目标状态
    while not len(sample_space) > 31:  # 初始化样本空间
        n = random.randint(0, pow(2, 32) - 1)
        t = '{:032b}'.format(n)
        if t not in sample_space:
            sample_space.append(t)


def fitness(sample):  # 适应度评价
    return difflib.SequenceMatcher(None, sample, target_data).ratio() * 1000


def selection():
    fit = []
    sample_fit = []
    global sample_space
    for i in sample_space:      # 测算每个个体的适应率
        f = fitness(i)
        if f == 1000:
            print(i)
            return True
        else:
            fit.append(f)

    for i in range(1, len(fit)):     # 构造轮盘
        fit[i] = fit[i] + fit[i - 1]

    for i in range(0, 16):  # 轮盘选择16个亲本进入下一代
        t = random.uniform(0, fit[-1])
        for j in fit:
            if t < j:
                ind = fit.index(j)
                sample_fit.append(sample_space[ind])
                break

    sample_space = sample_fit
    print(str(sample_space))
    return False


def cross():
    global sample_space

    for i in range(0, 16):      # 两两随机交换十六次
        m = random.randint(0, 15)
        n = random.randint(0, 15)
        p = random.randint(1, 31)
        sample_space.append(sample_space[m][0:p] + sample_space[n][p-1:31])


def mutations():    # 进行变异
    global sample_space

    r = random.randint(0, 100)
    if r < 20:
        m = random.randint(0, 31)
        n = random.randint(0, 31)
        s = sample_space[m][n]
        if s == '0':
            sample_space[m] = sample_space[m][:n - 1] + '1' + sample_space[m][n:]
        else:
            sample_space[m] = sample_space[m][:n - 1] + '0' + sample_space[m][n:]


if __name__ == '__main__':
    init()
    while not selection():
        cross()
        mutations()
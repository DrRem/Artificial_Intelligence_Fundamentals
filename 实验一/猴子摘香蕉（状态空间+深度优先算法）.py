# 状态空间法
# 猴子位置 箱子位置 香蕉位置 猴子是否在箱子上
target = [1, 1, 1, 1]  # 目标状态
initial = [0, 2, 1, 0]  # 初始状态
a = [[initial, 0]]  # 搜索栈
result = []  # 结果栈


# 猴子状态检查
def canmv(now):  # 检查猴子是否在箱子上
    if now[3] == 1:
        return False
    else:
        return True


def canmvleft(now):  # 猴子能否向左移动
    if now[0] > 0:
        return True
    else:
        return False


def canmvright(now):  # 猴子能否向右移动
    if now[0] < 2:
        return True
    else:
        return False


def boxcanmove(now):  # 检查盒子是否可以被移动
    if canmv(now):
        if now[0] == now[1]:
            return True
    return False


# 定义操作符
def monmvleft(now):  # 猴子左移
    now[0] = now[0] - 1
    print("The monkey moves one space to the left")
    return now


def momvright(now):  # 猴子右移
    now[0] = now[0] + 1
    print("The monkey moves one space to the right")
    return now


def boxmvleft(now):  # 箱子左移
    now[1] = now[1] - 1
    print("The box was pushed one space to the left by the monkey")
    now = monmvleft(now)
    return now


def boxmvright(now):  # 箱子右移
    now[1] = now[1] + 1
    print("The box was pushed one space to the left by the monkey")
    now = momvright(now)
    return now


def moclamp(now):  # 爬箱子
    now[3] = 1
    print("Monkey climbed up the box")
    return now


def moleave(now):  # 离开箱子
    now[3] = 0
    print("The monkey left the box")
    return now


# 构建搜索树
def trying():  # 将栈顶结点的有效后继节点全部入栈
    global a
    b = a.pop()
    deeps = b[1]
    deeps = deeps + 1
    before = b[0]
    if canmv(before.copy()):
        if canmvleft(before.copy()):
            after_left = monmvleft(before.copy())
            if after_left != before:
                a.append([after_left, deeps])
        if canmvright(before.copy()):
            after_right = momvright(before.copy())
            if after_right != before:
                a.append([after_right, deeps])
        if boxcanmove(before.copy()):
            after_clamp = moclamp(before.copy())
            a.append([after_clamp, deeps])
            if canmvleft(before.copy()):
                bafter_left = boxmvleft(before.copy())
                if bafter_left != before:
                    a.append([bafter_left, deeps])
            if canmvright(before.copy()):
                bafter_right = boxmvright(before.copy())
                if bafter_right != before:
                    a.append([bafter_right, deeps])
    else:
        after_leave = moleave(before.copy())
        a.append([after_leave, deeps])

    return deeps  # 返回当前深度


def DFS(deep):
    global a
    global result
    i = 0
    while len(a):
        if deep - 1 > a[-1][1]:
            if len(result):
                result.pop()
            while i < deep:  # 深度到达指定深度时停止
                result.append(a[-1])
                if result[-1][0] == target:
                    print("Monkey find banana:")
                    print(str(result))
                    exit(10)
                i = trying() + 1
        result.append(a.pop())
        if result[-1][0] == target:
            print("Monkey find banana:")
            print(str(result))
            exit(10)
        else:
            result.pop()
    print("Unable to find the answer at this depth")


if __name__ == "__main__":
    DFS(5)
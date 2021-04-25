# 八数码问题
Initial_state = [2, 8, 3, 1, 0, 4, 7, 6, 5]  # 初始状态
Goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]  # 目标状态
Result_stack = []  # 最终结果
temp_stack = [[Initial_state, 0]]  # 搜索用栈
appeared = [[Initial_state]]   # 查重栈


# 定义操作

def whereisvacancy(now):
    vacancy = now.index(0)
    return vacancy


def mvuptovac(now, vac):
    now[vac] = now[vac - 3]
    now[vac - 3] = 0
    return now


def mvdwtovac(now, vac):
    now[vac] = now[vac + 3]
    now[vac + 3] = 0
    return now


def mvltovac(now, vac):
    now[vac] = now[vac - 1]
    now[vac - 1] = 0
    return now


def mvrtovac(now, vac):
    now[vac] = now[vac + 1]
    now[vac + 1] = 0
    return now


def Hit_the_target(now):
    if now == Goal_state:
        return True
    else:
        return False


def structuresearch(top):
    global temp_stack
    now = top[0]
    deep = top[1]
    deep = deep + 1
    vac = whereisvacancy(now)
    if (vac + 1) % 3 == 0:
        noright = True
    else:
        noright = False
    if vac % 3 == 0:
        noleft = True
    else:
        noleft = False
    if (vac - 3) < 0:
        noup = True
    else:
        noup = False
    if (vac + 3) > 8:
        nodown = True
    else:
        nodown = False

    if not noup:
        atfer = mvuptovac(now.copy(), vac)
        if atfer not in appeared:
            temp_stack.append([atfer, deep])
            appeared.append(atfer)
    if not nodown:
        atfer = mvdwtovac(now.copy(), vac)
        if atfer not in appeared:
            temp_stack.append([atfer, deep])
            appeared.append(atfer)
    if not noleft:
        atfer = mvltovac(now.copy(), vac)
        if atfer not in appeared:
            temp_stack.append([atfer, deep])
            appeared.append(atfer)
    if not noright:
        atfer = mvrtovac(now.copy(), vac)
        if atfer not in appeared:
            temp_stack.append([atfer, deep])
            appeared.append(atfer)

    return deep


def DFS(deeps):
    global temp_stack
    global Result_stack
    Result_stack.append(temp_stack[-1])
    while len(temp_stack):
        if deeps - 1 == temp_stack[-1][1]:
            Result_stack.append(temp_stack.pop())
            if Hit_the_target(Result_stack[-1][0]):
                print("finish!")
                print(str(Result_stack))
                exit(10)
            else:
                Result_stack.pop()
        elif deeps - 1 > temp_stack[-1][1]:
            i = temp_stack[-1][1]
            if i <= Result_stack[-1][1]:
                while i <= Result_stack[-1][1]:
                    Result_stack.pop()
                    if len(Result_stack) == 0:
                        break
                while i < deeps - 1:
                    if len(temp_stack):
                        Result_stack.append(temp_stack[-1])
                        if Hit_the_target(Result_stack[-1][0]):
                            print("finish!")
                            print(str(Result_stack))
                            exit(10)
                        i = structuresearch(temp_stack.pop())
                    else:
                        break

    print("fall")


if __name__ == "__main__":
    DFS(5)  # 当深度大于等于5时有解

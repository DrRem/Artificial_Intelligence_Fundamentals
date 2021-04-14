BananaP = 1
MonkeyP = 0
BoxP = 2
OnBox = False


def monkey(moveto):  # 猴子移动
    if moveto == 0:
        print("monkey move to a")
    elif moveto == 1:
        print("monkey move to b")
    elif moveto == 2:
        print("monkey move to c")
    else:
        print("Monkey Error!")
        return False
    global MonkeyP
    MonkeyP = moveto
    return True


def boxCanMove():  # 判断猴子是否可以推箱子
    if MonkeyP == BoxP and not OnBox:
        return True
    else:
        return False


def box(moveto):  # 箱子移动
    if not boxCanMove():
        return False
    elif moveto == 0:
        print("box moved to a by monkey")
    elif moveto == 1:
        print("box moved to b by monkey")
    elif moveto == 2:
        print("box moved to c by monkey")
    else:
        print("Box Move Error!")
        return False
    global BoxP
    BoxP = moveto
    return True


def monkeyPushBox(moveto):  # 猴子推箱子
    box(moveto)
    monkey(moveto)


def clampBox():  # 猴子爬上箱子
    global OnBox
    OnBox = True
    print("monkey clamp box")
    return True


def leaveBox():  # 猴子爬下箱子
    global OnBox
    OnBox = False
    print("monkey leave box")
    return True


def ifSuccess():  # 判断是否能够够到香蕉
    if BoxP == BananaP == MonkeyP and OnBox:
        print("Monkey get banana!")
        return True
    else:
        print("unreachable!")
        return False


if __name__ == "__main__":
    a = input("Whether to initialize manually(yes/no):")

    if a == "yes":
        MonkeyP = int(input("Enter the initial position of the monkey(0~2):"))
        BoxP = int(input("Enter the initial position of the box(0~2):"))
        BananaP = int(input("Enter the initial position of the banana(0~2):"))
        if MonkeyP == BoxP:
            ifOnBox = input("Is the monkey on the box(yes/no):")
            if ifOnBox == "yes":
                OnBox = True
            else:
                OnBox = False
        else:
            OnBox = False

    print("monkey trying find banana ... ")

    if ifSuccess():  # 判断是否直接获得香蕉
        exit(1)
    if OnBox:  # 判断是否在盒子上
        leaveBox()
    if MonkeyP != BoxP:  # 判断是否在盒子附近
        monkey(moveto=BoxP)
    if BoxP != BananaP:  # 判断盒子是否在香蕉附近
        monkeyPushBox(moveto=BananaP)
    if not OnBox:  # 当在盒子旁边，盒子在香蕉旁边时候，爬箱子
        clampBox()
    ifSuccess()  # 获得香蕉

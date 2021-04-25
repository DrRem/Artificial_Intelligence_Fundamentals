import datetime

search_space = {  # 搜索空间
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D'],
}


def child_node(node, temp_list, appeared):
    for i in search_space[node]:
        if i not in appeared:
            temp_list.append(i)
            appeared.append(i)


def child_node_deeps(node, temp_list, appeared):
    now = node[0]
    deep = node[1]
    deep = deep + 1
    lenth = len(appeared)
    for i in search_space[now]:
        if i not in appeared:
            temp_list.append([i, deep])
            appeared.append(i)
    if lenth < len(appeared):
        return True
    else:
        return False


def BFS(target):  # 广度优先搜索
    result = []  # 结果栈
    temp = ['A']  # 搜索队列
    appeared = ['A']  # 查重栈
    while len(temp):
        result.append(temp[0])
        child_node(temp.pop(0), temp, appeared)
        if result[-1] == target:
            print(str(result))
            return True


def DFS(target):  # 深度优先搜索
    result = []  # 结果栈
    temp = [['A', 0]]  # 搜索队列
    appeared = []  # 查重栈
    result.append(temp[-1])
    if result[-1] == target:
        print(str(result))
        return True
    else:
        while len(temp):
            while child_node_deeps(temp.pop(), temp, appeared):
                result.append(temp[-1])
                if result[-1][0] == target:
                    print(str(result))
                    return True
            result.pop()
            result.append(temp[-1])
            if result[-1][0] == target:
                print(str(result))
                return True


if __name__ == "__main__":
    BFS('F')
    DFS('F')

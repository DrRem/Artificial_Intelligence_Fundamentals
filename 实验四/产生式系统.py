class Animal:
    def __init__(self):
        self.dict_before = {'1': '有毛发', '2': '产奶', '3': '有羽毛', '4': '会飞', '5': '会下蛋', '6': '吃肉', '7': '有犬齿',
                            '8': '有爪', '9': '眼盯前方', '10': '有蹄', '11': '反刍', '12': '黄褐色', '13': '有斑点', '14': '有黑色条纹',
                            '15': '长脖', '16': '长腿', '17': '不会飞', '18': '会游泳', '19': '黑白二色', '20': '善飞', '21': '哺乳类',
                            '22': '鸟类', '23': '食肉类', '24': '蹄类', '25': '金钱豹', '26': '虎', '27': '长颈鹿', '28': '斑马',
                            '29': '鸵鸟', '30': '企鹅', '31': '信天翁'}
        print('''输入对应条件前面的数字:
                                *******************************************************
                                *1:有毛发  2:产奶  3:有羽毛  4:会飞  5:会下蛋          *
                                *6:吃肉  7:有犬齿  8:有爪  9:眼盯前方  10:有蹄         *
                                *11:反刍  12:黄褐色  13:有斑点  14:有黑色条纹  15:长脖 *
                                *16:长腿  17:不会飞  18:会游泳  19:黑白二色  20:善飞   *
                                *21：哺乳类  22:鸟类  23:食肉类  24：蹄类              *
                                *******************************************************
                                *******************当输入数字0时!程序结束***************
            ''')
        # 各个特征的深度
        self.dict_depth = {'1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3, '10': 3, '11': 3,
                           '12': 2,
                           '13': 2, '14': 2, '15': 2, '16': 2,
                           '17': 2, '18': 2, '19': 2, '20': 2, '21': 2, '22': 2, '23': 2, '24': 2, '25': 1, '26': 1,
                           '27': 1,
                           '28': 1, '29': 1, '30': 1, '31': 1}
        # 规则集
        self.rules = [[[1], 21], [[2], 21], [[3], 22], [[6], 23], [[4, 5], 22], [[7, 8, 9], 23], [[10, 21], 24],
                      [[11, 21], 24],
                      [[12, 23, 14, 21], 26],
                      [[13, 15, 16, 24], 27], [[12, 13, 21, 23], 25], [[14, 24], 28], [[15, 17, 19, 22], 29],
                      [[17, 18, 19, 22], 30], [[20, 22], 31]]
        # 动物逆向推理优先级
        self.count = {'25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0, '31': 0}
        # 综合数据库
        self.list_real = []
        self.list = []
        while (1):
            # 循环输入前提条件所对应的字典中的键
            num_real = input("请输入：")
            if num_real == '0':
                break
            self.list_real.append(num_real)
            self.list.append(num_real)
        # print("\n")
        print("前提条件为：")
        # 输出前提条件
        for i in range(0, len(self.list_real)):
            print(self.dict_before[self.list_real[i]], end=" ")
        print("\n")
        print("推理结果如下：")

    # 求深度最小的进行改进的正向推演
    def min_depth(self):
        h = 100
        for i in range(len(self.list_real)):
            if h > int(self.dict_depth[self.list_real[i]]):
                h = int(self.dict_depth[self.list_real[i]])
        return h

    # 判断是否与数据基的数重复
    def judge_repeat(self, value):
        for i in range(0, len(self.list_real)):
            if self.list_real[i] == str(value):
                return 1
            else:
                m = len(self.list_real)
                if i != len(self.list_real) - 1:
                    continue
                else:
                    return 0

    # 进行改进的正向推理
    def forward(self, h):
        for j in range(len(self.list_real)):
            if int(self.dict_depth[self.list_real[j]]) == 2:
                for i in range(len(self.rules)):
                    if int(self.list_real[j]) in self.rules[i][0]:
                        if self.rules[i][1] in range(25, 32):
                            self.count[str(self.rules[i][1])] = self.count[str(self.rules[i][1])] + 1
                        if self.judge_repeat(self.rules[i][1]) == 0:
                            self.list_real.append(str(self.rules[i][1]))

    # 在正向推理的基础上进行逆向推理
    def backward(self, a):
        change = False
        for i in range(len(self.rules)):
            if a == self.rules[i][1]:
                for j in range(len(self.rules[i][0])):
                    change = False
                    m = self.rules[i][0][j]
                    if str(self.rules[i][0][j]) in self.list:
                        change = True
                        if j == len(self.rules[i][0]) - 1:
                            return change
                    else:
                        change = self.backward(int(self.rules[i][0][j]))
                        if not change:
                            break
        return change

    # 算法框架
    def run(self):
        self.forward(self.min_depth())
        self.count = sorted(self.count.items(), key=lambda d: d[1], reverse=True)
        for i in range(len(self.count)):
            if self.backward(int(self.count[i][0])):
                print("推理此动物为：", self.dict_before[str(self.count[i][0])])
                return
        print("无法推理此动物")
        return


# 主函数
if __name__ == '__main__':
    anmial = Animal()
    anmial.run()

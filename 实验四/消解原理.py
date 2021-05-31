S = []  # 以列表形式存储子句集S


def readClauseSet(filePath):
    global S
    for line in open(filePath, mode='r', encoding='utf-8'):
        line = line.replace(' ', '').strip()
        line = line.split('∨')
        S.append(line)


def opposite(clause):
    if '～' in clause:
        return clause.replace('～', '')
    else:
        return '～' + clause


def resolution():
    global S
    end = False
    while True:
        if end:
            break
        father = S.pop()
        for i in father[:]:
            if end:
                break
            for mother in S[:]:
                if end:
                    break
                j = list(filter(lambda x: x == opposite(i), mother))
                if not j:
                    continue
                else:
                    print('\n亲本子句：' + ' ∨ '.join(father) + ' 和 ' + ' ∨ '.join(mother))
                    father.remove(i)
                    mother.remove(j[0])
                    if father == [] and mother == []:
                        print('归结式：NIL')
                        end = True
                    elif not father:
                        print('归结式：' + ' ∨ '.join(mother))
                    elif not mother:
                        print('归结式：' + ' ∨ '.join(mother))
                    else:
                        print('归结式：' + ' ∨ '.join(father) + ' ∨ ' + ' ∨ '.join(mother))


def main():
    readClauseSet(r'test.txt')
    resolution()


if __name__ == '__main__':
main()

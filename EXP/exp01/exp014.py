import random


class animal:
    def __init__(self):  # 随机sex性别为male(1) or female(0)
        self.sex = random.randint(0, 1)

    def getSex(self):
        return self.sex


class bear(animal):
    def __init__(self):
        super().__init__()
        self.attack = 1

    def __repr__(self):
        if self.sex == 1:
            return 'male bear'
        else:
            return 'female bear'


class fish(animal):
    def __init__(self):
        super().__init__()
        self.attack = 0

    def __repr__(self):
        if self.sex == 1:
            return 'male fish'
        else:
            return 'female fish'


def river_generate(size):  # 长度为size的河流
    lst = []
    for i in range(size):
        num = random.randint(1, 3)
        if num == 1:
            lst.append(fish())
        elif num == 2:
            lst.append(bear())
        else:
            lst.append(None)
    return lst


def check(lst):  # 检查None的个数
    count = 0
    for i in lst:
        if i is None:
            count += 1
    if count == 0:
        return False  # 剩余空位不足无法新生成动物 故结束
    else:
        return True


class river:
    def __init__(self):
        self.lst = river_generate(10)

    def getList(self):
        return self.lst

    def bear_generate(self):
        if check(self.lst):
            n = 0
            while n < 1:  # 随机将列表中的None修改为熊
                item = random.choice(self.lst)
                if item is None:
                    temp = self.lst.index(item)
                    self.lst[temp] = bear()
                    n += 1
                    print(f'河流中{temp}位置生成了一只熊')

    def fish_generate(self):
        if check(self.lst):
            n = 0
            while n < 1:  # 随机将列表中的None修改为鱼
                item = random.choice(self.lst)
                if item is None:
                    temp = self.lst.index(item)
                    self.lst[temp] = fish()
                    n += 1
                    print(f'河流中{temp}位置生成了一只鱼')


class eco_system:
    def __init__(self):
        self.river = river()

    def getRiver(self):
        return self.river

    def tick(self):  # 1次运行
        lst = self.river.getList()
        for i in range(0, len(lst) - 1):
            num = random.randint(0, 1)
            if num == 0:  # num为0时生物尝试向右移动
                if isinstance(lst[i], bear):  # 熊的情况
                    animal1 = lst[i]
                    if isinstance(lst[i + 1], bear):  # 右边元素为熊 尝试交配
                        animal2 = lst[i + 1]
                        if animal1.getSex != animal2.getSex:
                            print(f'{i}和{i + 1}位置的公熊母熊相遇')
                            self.river.bear_generate()
                    elif isinstance(lst[i + 1], fish):  # 右边元素为鱼 熊把鱼吃掉
                        lst[i + 1] = animal1
                        lst[i] = None
                        print(f'{i}位置的熊走到{i + 1}位置吃掉了一条鱼')
                    elif lst[i + 1] is None:
                        lst[i + 1] = animal1
                        lst[i] = None
                        print(f'一只熊从{i}位置走到了{i + 1}位置')
                elif isinstance(lst[i], fish):  # 鱼的情况
                    animal1 = lst[i]
                    if isinstance(lst[i + 1], fish):  # 右边元素为鱼 尝试交配
                        animal2 = lst[i + 1]
                        if animal1.getSex != animal2.getSex:
                            print(f'{i}和{i + 1}位置的雌鱼和雄鱼相遇')
                            self.river.fish_generate()
                    elif isinstance(lst[i + 1], bear):  # 右边元素为熊 被吃掉了
                        lst[i] = None
                        print(f'可怜的{i}位置的鱼试图前进被吃掉了')
                    elif lst[i + 1] is None:
                        lst[i + 1] = animal1
                        lst[i] = None
                        print(f'一条鱼从{i}位置走到了{i + 1}位置')


def simulation(times):
    ecoSystem = eco_system()
    count = 0
    riverSimulation = ecoSystem.getRiver()
    currentRiver = riverSimulation.getList()
    print('初始河流：', end='')
    print(currentRiver)
    while check(currentRiver) and count < times:
        count += 1
        ecoSystem.tick()
        print(f'经过{count}次运行，河流目前为：', end='')
        print(currentRiver)
    if check(currentRiver) is False:
        print('None的个数不够 结束')
        return 0
    if count == times:
        print('运行结束')
        return 0


simulation(5)

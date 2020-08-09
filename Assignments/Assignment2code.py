# Options are mention after each statment
class Customer:  # a

    def __init__(self, id=0, name='No Name', points=0, grp='null', avg=0):  # b and c
        self.name = name
        self.points = points
        self.add = []
        self.avg = avg
        self.id = id
        self.grp = grp

    def addPoints(self, point: int):  # d
        self.add.append(point)
        self.points += point

    def upgradePoints(self, percent):  # e
        self.add.append(self.points * percent / 100)
        self.points = self.points * (1 + percent / 100)

    def removePoints(self, remove):  # f
        self.add.append(int(-remove))
        self.points -= remove
        if self.points < 0:
            self.points = 0

    def computeGroup(self):  # g
        if self.points < 100:
            self.grp = 'Silver'

        elif self.points >= 100 and self.points < 500:
            self.grp = 'Gold'

        elif self.points > 500 and self.points <= 2000:
            self.grp = 'Platinum'

        else:
            self.grp = 'Diamond'

    def display(self):  # h
        print(
            ' Id : {} \nName : {}\nPoints : {}\nGroup : {}\nAverage Points : {}'.format(self.id, self.name, self.points,
                                                                                        self.grp, self.avg))

    def calcAvg(self):
        sum2 = sum(self.add)
        self.avg = sum2 / len(self.add)

    def DisplayAvg(self):
        print(f'Average Value of points : {self.avg}')


class Test:  # l
    def main(self):
        self.c = []  # m
        self.c.append(Customer(1543, 'Nimal'))
        self.c.append(Customer(6561, 'Saman'))
        self.c.append(Customer(6954, 'Kasun'))
        self.c.append(Customer(3485, 'Nayana'))
        self.c.append(Customer(8546, 'Kalpa'))

        self.c[0].addPoints(129)  # n
        self.c[1].addPoints(785)
        self.c[2].addPoints(3258)
        self.c[3].addPoints(59)
        self.c[4].addPoints(1652)

        self.c[2].addPoints(1000)  # o

        self.c[1].upgradePoints(2)  # p

    def display(self):  # d
        for i, e in enumerate(self.c):
            print('Customer {}'.format(i + 1))
            e.display()
            print()
            print()

    def GetBest(self):  # k
        print(max(self.c, key=lambda x: x.points).id)


test = Test()
test.main()
test.display()  # r

for e in test.c:  # s
    e.calcAvg()
for e in test.c:  # t
    e.computeGroup()
test.display()  # u

test.GetBest()  # v

for e in test.c:  # w
    e.DisplayAvg()

cust = test.c[4]  # x y
cust.removePoints(2000)  # z
print()

test.c[4].display()  # aa
test.c[4].computeGroup()  # bb
test.c[4].calcAvg()  # cc

cust = Customer()  # dd
cust.name = test.c[4].name  # ee
cust.points = test.c[4].points
cust.grp = test.c[4].grp

cust1 = cust  # ff gg

del cust  # hh

print(cust1.id)  # ii

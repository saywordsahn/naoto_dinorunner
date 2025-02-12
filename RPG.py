class Player:

    def __init__(self, name):
        self.name = name
        self.attackdamage = 9999
        self.health = 10000

class Enemy:

    def __init__(self, type):
        self.type = type
        self.attackdamage = 100
        self.health = 100

        if type == 'skeleton':
            self.attackdamage = 150
            self.health = 125

        elif type == 'enderman':
            self.attackdamage = 300
            self.health = 500


p1 = Player('steve')
print(p1.name)
e1 = Enemy('zombie')
e2 = Enemy('skeleton')
e3 = Enemy('enderman')
print(e1.type, e2.type, e3.type)
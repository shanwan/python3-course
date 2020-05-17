import random


class Enemy:
    hp = 200

    def __init__(self, attacklow, attackhigh):
        self.attacklow = attacklow
        self.attackhigh = attackhigh

    def getAttack(self):
        print("Attack is ",self.attacklow)

    def getHp(self):
        print("Hp is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getAttack()
enemy1.getHp()

enemy2 = Enemy(50, 59)
enemy2.getAttack()
enemy2.getHp()

'''
playerhp = 260
enemyattacklow = 60
enemyattackhigh = 80

while playerhp > 0:
    damage = random.randrange(enemyattacklow, enemyattackhigh)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes ",damage ,"damage points.You have ",playerhp ," hp left.")

    if playerhp == 30:
        print("You have low health. You have been teleported to a hospital.")
        break
'''

from numpy.random import randint

class Character():
	def __init__(self, name, hp, attack, defence, agility):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.defence = defence
		self.agility = agility

c1 = Character('勇者', 150, 60, 40, 60)
c2 = Character('スライム', 100, 40, 20, 30)

for k,v in c1.__dict__.items():
	print(k, v)

for k,v in c2.__dict__.items():
	print(k, v)

def damage_calc(c1, c2):
	base = c1.attack // 2 - c2.defence // 4
	rand = base // 16 + 1
	tmp = randint(0, rand * 2 + 1) - rand
	damage = base + tmp
	return damage

def agility_calc(c):
	base = c.agility
	tmp = base // 10
	result = randint(base - tmp, base + tmp + 1)
	return result

def turn_calc(c1, c2):
	a1 = agility_calc(c1)
	a2 = agility_calc(c2)
	if a1 >= a2:
		return True
	else:
		return False

# ターン中の計算
def turn(c1, c2):
	# 勇者のターン
	damage = damage_calc(c1, c2)
	c2.hp = c2.hp - damage if c2.hp - damage >= 0 else 0
	print('{0}の攻撃:{1}に{2}のダメージ'.format(c1.name, c2.name, damage))
	print('{0}のHP:{1}'.format(c2.name, c2.hp))
	if c2.hp <= 0:
		print('{0}は力尽きた'.format(c2.name))
		return(c1, c2, 0)

	# スライムのターン
	damage = damage_calc(c2, c1)
	c1.hp = c1.hp - damage if c1.hp - damage >= 0 else 0
	print('{0}の攻撃:{1}に{2}のダメージ'.format(c2.name, c1.name, damage))
	print('{0}のHP:{1}'.format(c1.name, c1.hp))
	if c1.hp <= 0:
		print('{0}は力尽きた'.format(c1.name))
		return(c1, c2, 1)
	return(c1, c2, 9)

# 戦闘
def battle(c1, c2):
	while True:
		# 勇者が先のターン
		if turn_calc(c1, c2):
			c1, c2, flg = turn(c1, c2)
		# スライムが先のターン
		else:
			c2, c1, flg = turn(c2, c1)
		if flg == 0:
			print('finish : {0}の勝ち!'.format(c1.name))
			break
		elif flg == 1:
			print('finish : {0}の勝ち!'.format(c2.name))
			break

battle(c1, c2)
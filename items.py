class item:
	def __init__(self, name, itemAction, param1=0):
		self.name = name
		self.itemAction = itemAction
		if itemAction == 'heal':
			self.hp = param1
		if itemAction == 'revive':
			self.hp = param1

potion = item('Potion', 'heal', 20)
hyperpotion = item('HyperPotion', 'heal', 50)
revive = item('Revive', 'revive', 500 )




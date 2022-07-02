class pokeType():
	def __init__(self, name, weakness, resistance, no_effect, color):
		self.name = name
		self.weakness = weakness
		self.resistance = resistance
		self.no_effect = no_effect
		self.color = color


waterType = pokeType('Water', {'Grass', 'Electric'}, {'Steel', 'Fire', 'Water', 'Ice'}, {'None'}, '#0000ff')
grassType = pokeType('Grass', {'Fire', 'Ice', 'Flying', 'Bug', 'Poison'}, {'Water', 'Grass', 'Electric'}, {'None'}, '#00ff00')
fireType = pokeType('Fire', {'Water', 'Ground', 'Rock'}, {'Bug', 'Steel', 'Fire', 'Grass', 'Ice', 'Fairy'}, {'None'}, '#ff0000')
electricType = pokeType('Electric', {'Ground'}, {'Flying', 'Steel', 'Electric'}, 'None', '#f7dc6f')
psychicType = pokeType('Psychic', {'Bug', 'Ghost', 'Dark', 'Psychic'}, {'Fighting'}, {'None'}, '#ff00ff')
iceType = pokeType('Ice', {'Fighting', 'Rock', 'Steel', 'Fire'}, {'Ice'}, 'None', '#40fbe2')
dragonType = pokeType('Dragon', {'Ice', 'Dragon', 'Fairy'}, {'Fire', 'Water', 'Grass', 'Electric'}, {'None'}, '#3f3d93')
darkType = pokeType('Dark', {'Fighting', 'Bug', 'Fairy'}, {'Ghost', 'Dark'}, {'Psychic'}, '#000000')
fairyType = pokeType('Fairy', {'Poison', 'Steel'}, {'Fighting', 'Bug', 'Dark'}, {'Dragon'}, '#ffa3e9')
normalType = pokeType('Normal', {'Fighting'}, {'None'}, {'Ghost'}, '#d7dbdd')
fightingType = pokeType('Fighting', {'Flying', 'Psychic', 'Fairy'}, {'Rock', 'Bug', 'Dark'}, {'None'}, '#de3163')
flyingType = pokeType('Flying', {'Rock', 'Electric', 'Ice'}, {'Fighting', 'Bug', 'Grass'}, {'Ground'}, '#ccccff')
poisonType = pokeType('Poison', {'Ground', 'Psychic'}, {'Fighting', 'Poison', 'Bug', 'Grass', 'Fairy'}, {'None'}, '#8e00fc')
groundType = pokeType('Ground', {'Water', 'Grass', 'Ice'}, {'Poison', 'Rock'}, {'Electric'}, '#b28930')
rockType = pokeType('Rock', {'Fighting', 'Ground', 'Steel', 'Water', 'Grass'}, {'Normal', 'Flying', 'Poison', 'Fire'}, {'None'}, '#d7a624')
bugType = pokeType('Bug', {'Flying', 'Rock', 'Fire'}, {'Fighting', 'Ground', 'Grass'}, {'None'}, '#83ba3e')
ghostType = pokeType('Ghost', {'Ghost', 'Dark'}, {'Poison', 'Bug'}, {'Normal', 'Fighting'}, '#310956')
steelType = pokeType('Steel', {'Fighting', 'Ground', 'Fire'}, {'Normal', 'Flying', 'Rock', 'Bug', 'Steel', 'Grass', 'Psychic', 'Ice', 'Dragon', 'Fairy'}, {'Poison'}, '#999999')




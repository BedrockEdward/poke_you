class pokeType():
	def __init__(self, name, weakness, resistance, no_effect, color):
		self.name = name
		self.weakness = weakness
		self.resistance = resistance
		self.no_effect = no_effect
		self.color = color


waterType = pokeType('Water', {'Grass', 'Electric', 'Love'}, {'Steel', 'Fire', 'Water', 'Ice'}, {'None'}, '#0000ff')
grassType = pokeType('Grass', {'Fire', 'Ice', 'Flying', 'Love', 'Bug', 'Poison'}, {'Water', 'Grass', 'Electric'}, {'None'}, '#00ff00')
fireType = pokeType('Fire', {'Water', 'Ground', 'Rock', 'Love'}, {'Bug', 'Steel', 'Fire', 'Grass', 'Ice', 'Fairy'}, {'None'}, '#ff0000')
electricType = pokeType('Electric', {'Ground'}, {'Flying','Love', 'Steel', 'Electric'}, 'None', '#f7dc6f')
psychicType = pokeType('Psychic', {'Bug', 'Ghost', 'Dark','Love', 'Psychic'}, {'Fighting'}, {'None'}, '#ff00ff')
iceType = pokeType('Ice', {'Fighting', 'Rock', 'Steel', 'Fire', 'Love' }, {'Ice'}, 'None', '#40fbe2')
dragonType = pokeType('Dragon', {'Ice', 'Dragon', 'Fairy', 'Love'}, {'Fire', 'Water', 'Grass', 'Electric'}, {'None'}, '#3f3d93')
darkType = pokeType('Dark', {'Fighting', 'Bug', 'Fairy', 'Love'}, {'Ghost', 'Dark'}, {'Psychic'}, '#000000')
fairyType = pokeType('Fairy', {'Poison', 'Steel', 'Love'}, {'Fighting', 'Bug', 'Dark'}, {'Dragon'}, '#ffa3e9')
normalType = pokeType('Normal', {'Fighting', 'Love'}, {'None'}, {'Ghost'}, '#d7dbdd')
fightingType = pokeType('Fighting', {'Flying', 'Psychic', 'Fairy', 'Love'}, {'Rock', 'Bug', 'Dark'}, {'None'}, '#de3163')
flyingType = pokeType('Flying', {'Rock', 'Electric', 'Ice', 'Love'}, {'Fighting', 'Bug', 'Grass'}, {'Ground'}, '#ccccff')
poisonType = pokeType('Poison', {'Ground', 'Psychic', 'Love'}, {'Fighting', 'Poison', 'Bug', 'Grass', 'Fairy'}, {'None'}, '#8e00fc')
groundType = pokeType('Ground', {'Water', 'Grass', 'Ice', 'Love'}, {'Poison', 'Rock'}, {'Electric'}, '#b28930')
rockType = pokeType('Rock', {'Fighting', 'Ground', 'Steel', 'Water', 'Grass', 'Love'}, {'Normal', 'Flying', 'Poison', 'Fire'}, {'None'}, '#d7a624')
bugType = pokeType('Bug', {'Flying', 'Rock', 'Fire', 'Love'}, {'Fighting', 'Ground', 'Grass'}, {'None'}, '#83ba3e')
ghostType = pokeType('Ghost', {'Ghost', 'Dark', 'Love'}, {'Poison', 'Bug'}, {'Normal', 'Fighting'}, '#310956')
steelType = pokeType('Steel', {'Fighting', 'Ground', 'Fire', 'Love'}, {'Normal', 'Flying', 'Rock', 'Bug', 'Steel', 'Grass', 'Psychic', 'Ice', 'Dragon', 'Fairy'}, {'Poison'}, '#999999')
loveType = pokeType('Love', {'Normal'},{'Normal'},{'Water', 'Grass', 'Fire', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel'}, '#ffa3e9')
hateType = pokeType('Hate', {'Water', 'Grass', 'Fire', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel'},{'Water', 'Grass', 'Fire', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel'},{'Normal'}, '#ffa3e9')

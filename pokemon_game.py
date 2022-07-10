
# To Do
'''
Bench
	Switch pokemon
Turns
Explosion move type
Status Effects
Type Icons
-Save Game-

4 moves

Edward: 
George: 
'''

import tkinter as tk
from random import randint

# Pokemon Code Libraries
from pokedex import pokemon_list, pokemon

# Multiply the hp
hpMultiplier = 5

# Create a window
root = tk.Tk()
root.title("pokemon-battle")
#root.geometry("19200x1080")

# Create squares in the window
headerFrame = tk.Frame(root, width=100)
activeFrame = tk.Frame(root)
cardFrameL = tk.Frame(activeFrame, width=100, height=200, bg="#ffafff")
cardFrameR = tk.Frame(activeFrame, width=100, height=200, bg="#ffafff")
benchFrameL = tk.Frame(root, width=212, height=200, bg="#ffffff")
benchFrameR = tk.Frame(root, width=212, height=200, bg="#ffffff")
buttonFrame = tk.Frame(root)
buttonFrameL = tk.Frame(buttonFrame, width=100)
buttonFrameR = tk.Frame(buttonFrame, width=100)
cardFrameL.pack_propagate(0)
cardFrameR.pack_propagate(0)

# Player and his pokemon
class PlayerSide:
	def __init__(self, side, cardFrame, benchFrame):
		self.side = side
		self.bench = []
		self.activePokemon = self.makePokemon()
		self.buildBench(6)
		self.cardFrame = cardFrame
		self.benchFrame = benchFrame

	# Create a bench with 5 random pokemon
	def buildBench(self, numPokemon):
		for p in range(0,numPokemon-1):
			newPokemon = self.makePokemon()
			self.bench.append(newPokemon)
	
	# Choose a random pokemon
	def makePokemon(self):
		pokemon_num = randint(0, len(pokemon_list)-1)
		newPokemon = pokemon(pokemon_list[pokemon_num].name,
							pokemon_list[pokemon_num].type,
							pokemon_list[pokemon_num].type2,
							pokemon_list[pokemon_num].hp * hpMultiplier,
							pokemon_list[pokemon_num].move1,
							pokemon_list[pokemon_num].move2,
							pokemon_list[pokemon_num].move3)
		return newPokemon


# Game structure
class GameInstance:
	# Initialize players and draw their cards
	def __init__(self):
		self.left = PlayerSide('left', cardFrameL, benchFrameL)
		self.right = PlayerSide('right', cardFrameR, benchFrameR)
		minusCard(buttonFrame)
		self.makeCards(self.left, self.right)
		self.makeCards(self.right, self.left)

	# Draw or redraw all of a player's cards
	def makeCards(self, player, opponent):
		self.makeCard(player.activePokemon, player, opponent)
		for bp in range(len(player.bench)):
			self.makeCard(player.bench[bp], player, opponent, bp)


	# Make a card and give it a name, hp, and attacks
	def makeCard(self, pokemonEntity, player, opponent, benchSpot=6):
		cardFrame = player.cardFrame
		if benchSpot < 6:
			cardFrame = player.benchFrame
		card = tk.Frame(cardFrame, width=100, height=200, highlightbackground="#ffafff", highlightthickness=1, bg=pokemonEntity.type.color)
		card.pack_propagate(0)

		# Build the card with attacks
		card.pack(side=player.side, padx=3)
		hp = tk.Label(card, text=pokemonEntity.hp, width=100, font='Helvetica 20 bold', bg="#ff0fff")
		hp.pack()
		pokeName = tk.Label(card, text=pokemonEntity.name, font='Helvetica 10 bold', bg="#ffafff")
		pokeName.pack()
		attackButton(card, player, pokemonEntity.move1, opponent, benchSpot)
		attackButton(card, player, pokemonEntity.move2, opponent, benchSpot)
		attackButton(card, player, pokemonEntity.move3, opponent, benchSpot)

		# Add a Switch button if the pokemon is on the bench
		if ((benchSpot < 6) and (pokemonEntity.hp > 0)):
			switchButton = tk.Button(card, width=20, text='Switch', font='Helvetica 10 bold',
				command=lambda:self.switchPokemon(pokemonEntity, player, benchSpot, opponent))
			switchButton.pack(side='bottom')

	# Switch a benched pokemon with the active pokemon
	def switchPokemon(self, pokemonEntity, player, benchSpot, opponent):
		player.bench.append(player.activePokemon)
		player.activePokemon = pokemonEntity
		player.bench.pop(benchSpot)
		minusCard(player.cardFrame)
		minusCard(player.benchFrame)
		game.makeCards(player, opponent)


# Create an attack button
def attackButton(card, player, move, opponent, benchSpot):
	moveButton = tk.Button(card, width=20, fg=move.type.color, text=move.name, font='Helvetica 10 bold',
		command=lambda:moveAttack(player, move, opponent, benchSpot))
	moveButton.pack()


# Attack the pokemon by reducing the hp, clearing the cards, and then making them again
def moveAttack(player, move, opponent, benchSpot):
	# Check if Benched
	if (opponent.activePokemon == None) or (player.activePokemon.hp==0) or (opponent.activePokemon.hp == 0) or (benchSpot < 6):
		return
	moveChance = randint(0, 99)
	damageHit = move.damage
	effectiveText = ''
	if move.accuracy < moveChance:
		damageHit = 0
		effectiveText = 'It missed.'

	if damageHit > 0:
		for weakness in opponent.activePokemon.type.weakness:
			if weakness == move.type.name:
				damageHit=damageHit*2
		for resistance in opponent.activePokemon.type.resistance:		
			if resistance == move.type.name:
				damageHit=damageHit/2
		for no_effect in opponent.activePokemon.type.no_effect:		
			if no_effect == move.type.name:
				damageHit=0

		if (damageHit > 0) and (opponent.activePokemon.type2 != None):
			for weakness in opponent.activePokemon.type2.weakness:
				if weakness == move.type.name:
					damageHit=damageHit*2
			for resistance in opponent.activePokemon.type2.resistance:		
				if resistance == move.type.name:
					damageHit=damageHit/2
			for no_effect in opponent.activePokemon.type2.no_effect:		
				if no_effect == move.type.name:
					damageHit=0
				
		if damageHit > move.damage:
			effectiveText = 'It was super effective.'
		if damageHit < move.damage:
			effectiveText = 'It was not very effective.'
		if damageHit == 0:
			effectiveText = 'It did no damage.'
		opponent.activePokemon.hp = opponent.activePokemon.hp - damageHit

	moveText = player.activePokemon.name + ' used ' + move.name + '. ' + effectiveText
	if move.moveAction == 'drain':
		player.activePokemon.hp = player.activePokemon.hp + (damageHit/2)
	if move.moveAction == 'superdrain':
		player.activePokemon.hp = player.activePokemon.hp + (damageHit*9999999)

	# Redraw cards after performing the attack
	minusCard(player.cardFrame)
	minusCard(opponent.cardFrame)
	if player.activePokemon.hp < 0:
		player.activePokemon.hp = 0
	game.makeCard(player.activePokemon, player, opponent)
	if opponent.activePokemon.hp < 0:	
		opponent.activePokemon.hp = 0
	game.makeCard(opponent.activePokemon, opponent, player)

	if opponent.activePokemon.hp == 0:
		effectiveText = effectiveText + ' ' + opponent.activePokemon.name + ' fainted.'
	moveText = player.activePokemon.name+ ' used ' + move.name + '. ' + effectiveText

	# Draw the battle text at the top of the screen
	minusCard(headerFrame)
	title = tk.Label(headerFrame, text=moveText, font='Helvetica 14 bold', fg=move.type.color)
	title.pack(side="top")


# Basic function for clearing cards
def minusCard(cardFrame):
	for thing in cardFrame.winfo_children():
		thing.destroy()

# Create the game instance so we can call it later
def startGame():
	global game
	game = GameInstance()

# Add and remove buttons
headerFrame.config(bg="#ffafff")
startButton = tk.Button(buttonFrame, width=15, height=5, fg="#ffafff", text="Start!", font='Helvetica 20 bold', command=startGame)

# Tkinter UI packing
title = tk.Label(headerFrame, text="Pokemon Battle", font='Helvetica 18 bold')
title.pack(side="top")
startButton.pack(side="left")
headerFrame.pack(side="top", pady=10)
activeFrame.pack()
cardFrameL.pack(side="left", pady=50)
cardFrameR.pack(side="right", pady=50)
benchFrameL.pack(side="left", pady=50)
benchFrameR.pack(side="right", pady=50)
buttonFrame.pack(side="bottom")

# Run the program!
root.mainloop()



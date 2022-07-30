
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
from attack import attackButton
from utils import minusCard
import items
# Multiply the hp
hpMultiplier = 5



# Player and his pokemon
class PlayerSide:
	def __init__(self, side, cardFrame, benchFrame, itemFrame):
		self.side = side
		self.bench = []
		self.activePokemon = self.makePokemon()
		self.buildBench(6)
		self.cardFrame = cardFrame
		self.benchFrame = benchFrame
		self.itemFrame = itemFrame
		self.buildBag()
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
							pokemon_list[pokemon_num].movelist)
		return newPokemon

	def buildBag(self):
		self.bag =[items.potion]
		self.bag =[items.hyperpotion]
		self.bag =[items.revive]
# Game structure
class GameInstance:
	# Initialize players and draw their cards
	def __init__(self):
		self.left = PlayerSide('left', cardFrameL, benchFrameL, itemFrameL)
		self.right = PlayerSide('right', cardFrameR, benchFrameR, itemFrameR)
		minusCard(buttonFrame)
		self.makeCards(self.left, self.right)
		self.makeCards(self.right, self.left)
		self.makeItemCards(self.right, self.left)
		self.makeItemCards(self.left, self.right)
		self.makeItemCards(self.left, self.right)
	def makeItemCards(self, player, opponent):
		itemButton = tk.Button(player.itemFrame, width=20, text=player.bag[0].name, font='Helvetica 10 bold',
			command=lambda:useItem(self, player, opponent, player.bag[0]))
		itemButton.pack(side='top')




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
		card = tk.Frame(cardFrame, width=100, height=250, highlightbackground="#ffafff", highlightthickness=1, bg=pokemonEntity.type.color)
		card.pack_propagate(0)

		# Build the card with attacks
		card.pack(side=player.side, padx=3)
		hp = tk.Label(card, text=pokemonEntity.hp, width=100, font='Helvetica 20 bold', bg="#ff0fff")
		hp.pack()
		pokeName = tk.Label(card, text=pokemonEntity.name, font='Helvetica 10 bold', bg="#ffafff")
		pokeName.pack()
		attackButton(card, player, pokemonEntity.move1, opponent, benchSpot, self, headerFrame)
		attackButton(card, player, pokemonEntity.move2, opponent, benchSpot, self, headerFrame)
		attackButton(card, player, pokemonEntity.move3, opponent, benchSpot, self, headerFrame)
		attackButton(card, player, pokemonEntity.move4, opponent, benchSpot, self, headerFrame) 

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


def useItem(game, player, opponent, item):
	if item.itemAction =='heal':
		player.activePokemon.hp += item.hp
	if item.itemAction =='revive':
		player.activePokemon.hp += item.hp
	minusCard(player.cardFrame)
	minusCard(opponent.cardFrame)
	if player.activePokemon.hp < 0:
		player.activePokemon.hp = 0
	game.makeCard(player.activePokemon, player, opponent)
	if opponent.activePokemon.hp < 0:	
		opponent.activePokemon.hp = 0
	game.makeCard(opponent.activePokemon, opponent, player)

	
	moveText = player.activePokemon.name+ ' used ' + item.name + '. '

# Draw the battle text at the top of the screen
	minusCard(headerFrame)
	title = tk.Label(headerFrame, text=moveText, font='Helvetica 14 bold', fg='black')
	title.pack(side="top")

# Create the game instance so we can call it later
def startGame():
	global game
	game = GameInstance()

# Create a window
root = tk.Tk()
root.title("pokemon-battle")
#root.geometry("19200x1080")

# Create squares in the window

headerFrame = tk.Frame(root, width=100)
activeFrame = tk.Frame(root)




itemFrameL = tk.Frame(activeFrame, bg = "#ffffff", width=100, height=250)
itemFrameR = tk.Frame(activeFrame, bg = "#ffffff", width=100, height=250)
itemTitleL = tk.Label(itemFrameL, text="Items",width=100, font='Helvetica 10 bold', bg="#ffafff")
itemTitleR = tk.Label(itemFrameR, text="Items",width=100, font='Helvetica 10 bold', bg="#ffafff")




cardFrameL = tk.Frame(activeFrame, width=100, height=250, bg="#ffafff")
cardFrameR = tk.Frame(activeFrame, width=100, height=250, bg="#ffafff")
benchFrameL = tk.Frame(root, width=212, height=250, bg="#ffffff")
benchFrameR = tk.Frame(root, width=212, height=250, bg="#ffffff")
buttonFrame = tk.Frame(root)
buttonFrameL = tk.Frame(buttonFrame, width=100)
buttonFrameR = tk.Frame(buttonFrame, width=100)
cardFrameL.pack_propagate(0)
cardFrameR.pack_propagate(0)

# Add and remove buttons
headerFrame.config(bg="#ffafff")
startButton = tk.Button(buttonFrame, width=15, height=5, fg="#ffafff", text="Start!", font='Helvetica 20 bold', command=startGame)

# Tkinter UI packing
title = tk.Label(headerFrame, text="Pokemon Battle", font='Helvetica 18 bold')
title.pack(side="top")
startButton.pack(side="left")
headerFrame.pack(side="top", pady=10)
activeFrame.pack()
itemFrameR.pack_propagate(0)
itemFrameL.pack_propagate(0)
itemFrameR.pack(side="right")
itemFrameL.pack(side="left")
itemTitleR.pack(side="top")
itemTitleL.pack(side="top")
cardFrameL.pack(side="left", pady=50)
cardFrameR.pack(side="right", pady=50)
benchFrameL.pack(side="left", pady=50)
benchFrameR.pack(side="right", pady=50)
buttonFrame.pack(side="bottom")

# Run the program!
root.mainloop()



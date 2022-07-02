
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

# Make a dummy pokemon just to fill the space
newPokemon = pokemon(pokemon_list[0].name,
	pokemon_list[0].type,
	pokemon_list[0].type2,
	pokemon_list[0].hp,
	pokemon_list[0].move1,
	pokemon_list[0].move2,
	pokemon_list[0].move3
)
active_pokemonR = newPokemon
active_pokemonL = newPokemon

bench_pokemonR = [newPokemon, newPokemon, newPokemon, newPokemon, newPokemon]
bench_pokemonL = [newPokemon, newPokemon, newPokemon, newPokemon, newPokemon]

startL = True
startR = True


# Choose a random pokemon and make the card
def newPoke(cardFrame):
	global startL
	global startR
	global active_pokemonL
	global active_pokemonR
	global bench_pokemonL
	global bench_pokemonR

	# Choose a random pokemon
	pokemon_num = randint(0, len(pokemon_list)-1)
	newActivePokemon = pokemon(pokemon_list[pokemon_num].name,
						pokemon_list[pokemon_num].type,
						pokemon_list[pokemon_num].type2,
						pokemon_list[pokemon_num].hp * hpMultiplier,
						pokemon_list[pokemon_num].move1,
						pokemon_list[pokemon_num].move2,
						pokemon_list[pokemon_num].move3
					)



	# Make the card
	if cardFrame == cardFrameL:
		active_pokemonL = newActivePokemon
		active_pokemon = active_pokemonL
		bench_pokemon = bench_pokemonL
		benchFrame = benchFrameL
		start = startL
	else:
		active_pokemonR = newActivePokemon
		active_pokemon = active_pokemonR
		bench_pokemon = bench_pokemonR
		benchFrame = benchFrameR
		start = startR
	makeCard(active_pokemon, cardFrame)

	minusCard(benchFrame)


	# Make Bench
	if start:
		bench_pokemon[0] = makeBenchPokemon()
		bench_pokemon[0].benchPlace = 1
		bench_pokemon[1] = makeBenchPokemon()
		bench_pokemon[1].benchPlace = 2
		bench_pokemon[2] = makeBenchPokemon()
		bench_pokemon[2].benchPlace = 3
		bench_pokemon[3] = makeBenchPokemon()
		bench_pokemon[3].benchPlace = 4
		bench_pokemon[4] = makeBenchPokemon()
		bench_pokemon[4].benchPlace = 5
		if cardFrame == cardFrameL:
			startL = False
		else:
			startR = False

	makeCard(bench_pokemon[0], benchFrame)
	makeCard(bench_pokemon[1], benchFrame)
	makeCard(bench_pokemon[2], benchFrame)
	makeCard(bench_pokemon[3], benchFrame)
	makeCard(bench_pokemon[4], benchFrame)

	newPokeText = 'Go ' + active_pokemon.name + '.'

	minusCard(headerFrame)
	title = tk.Label(headerFrame, text=newPokeText, font='Helvetica 14 bold')
	title.pack(side="top")
	

def makeBenchPokemon():
	pokemon_num = randint(0, len(pokemon_list)-1)
	newBenchPokemon = pokemon(pokemon_list[pokemon_num].name,
						pokemon_list[pokemon_num].type,
						pokemon_list[pokemon_num].type2,
						pokemon_list[pokemon_num].hp * hpMultiplier,
						pokemon_list[pokemon_num].move1,
						pokemon_list[pokemon_num].move2,
						pokemon_list[pokemon_num].move3,
						True
					)
	return newBenchPokemon


# Make a card and give it a name, hp, and attacks
def makeCard(active_pokemon, cardFrame):
	card = tk.Frame(cardFrame, width=100, height=200, highlightbackground="#ffafff", highlightthickness=1, bg=active_pokemon.type.color)
	card.pack_propagate(0)

	# Set parameters depending on the side
	if cardFrame == cardFrameL:
		side_ = 'right'
		defending_pokemon = active_pokemonR
		defPokeCardFrame = cardFrameR
		switch_active = active_pokemonL
	elif cardFrame == cardFrameR:
		side_ = 'left'
		defending_pokemon = active_pokemonL
		defPokeCardFrame = cardFrameL
		switch_active = active_pokemonR
	elif cardFrame == benchFrameR:
		side_ = 'left'
		defending_pokemon = None
		defPokeCardFrame = cardFrameR
		switch_active = active_pokemonR
		benchFrame = benchFrameR
	else:
		side_ = 'left'
		defending_pokemon = None
		defPokeCardFrame = cardFrameL
		switch_active = active_pokemonL
		benchFrame = benchFrameL


	# Build the card
	card.pack(side=side_, padx=3)
	hp = tk.Label(card, text=active_pokemon.hp, width=100, font='Helvetica 20 bold', bg="#ff0fff")
	hp.pack()
	pokeName = tk.Label(card, text=active_pokemon.name, font='Helvetica 10 bold', bg="#ffafff")
	pokeName.pack()
	attackButton(card, active_pokemon.move1, defending_pokemon, defPokeCardFrame, active_pokemon)
	attackButton(card, active_pokemon.move2, defending_pokemon, defPokeCardFrame, active_pokemon)
	attackButton(card, active_pokemon.move3, defending_pokemon, defPokeCardFrame, active_pokemon)

	if (active_pokemon.bench and (active_pokemon.hp > 0)):
		switchButton = tk.Button(card, width=20, text='Switch', font='Helvetica 10 bold',
			command=lambda:switchPokemon(switch_active, active_pokemon, defPokeCardFrame, benchFrame))
		switchButton.pack(side='bottom')

def switchPokemon(active_pokemon, switch_pokemon, cardFrame, benchFrame):
	global active_pokemonL
	global active_pokemonR
	global bench_pokemonL
	global bench_pokemonR

	active_pokemon.bench = True
	switch_pokemon.bench = False
	if cardFrame == cardFrameL:
		bench_pokemonL[switch_pokemon.benchPlace-1] = active_pokemon
		active_pokemonL = switch_pokemon
		active_pokemonL.benchPlace = 0
		bench_pokemon = bench_pokemonL
		active_pokemon = active_pokemonL

	else:
		bench_pokemonR[switch_pokemon.benchPlace-1] = active_pokemon
		active_pokemonR = switch_pokemon
		active_pokemonR.benchPlace = 0
		bench_pokemon = bench_pokemonR
		active_pokemon = active_pokemonR
	minusCard(cardFrame)
	minusCard(benchFrame)

	makeCard(active_pokemon, cardFrame)
	makeCard(bench_pokemon[0], benchFrame)
	makeCard(bench_pokemon[1], benchFrame)
	makeCard(bench_pokemon[2], benchFrame)
	makeCard(bench_pokemon[3], benchFrame)
	makeCard(bench_pokemon[4], benchFrame)

# Create an attack button
def attackButton(card, move, defending_pokemon, defPokeCardFrame, active_pokemon):
	moveButton = tk.Button(card, width=20, fg=move.type.color, text=move.name, font='Helvetica 10 bold',
		command=lambda:moveAttack(active_pokemon, defending_pokemon, defPokeCardFrame, move))
	moveButton.pack()


# Attack the pokemon by reducing the hp, clearing the cards, and then making them again
def moveAttack(active_pokemon, defending_pokemon, cardFrame, move):
	# Check if Benched
	if (defending_pokemon == None) or (active_pokemon.hp==0) or (defending_pokemon.hp == 0):
		return
	moveChance = randint(0, 99)
	damageHit = move.damage
	effectiveText = ''
	if move.accuracy < moveChance:
		damageHit = 0
		effectiveText = 'It missed.'

	if damageHit > 0:
		for weakness in defending_pokemon.type.weakness:
			if weakness == move.type.name:
				damageHit=damageHit*2
		for resistance in defending_pokemon.type.resistance:		
			if resistance == move.type.name:
				damageHit=damageHit/2
		for no_effect in defending_pokemon.type.no_effect:		
			if no_effect == move.type.name:
				damageHit=0

		if (damageHit > 0) and (defending_pokemon.type2 != None):
			for weakness in defending_pokemon.type2.weakness:
				if weakness == move.type.name:
					damageHit=damageHit*2
			for resistance in defending_pokemon.type2.resistance:		
				if resistance == move.type.name:
					damageHit=damageHit/2
			for no_effect in defending_pokemon.type2.no_effect:		
				if no_effect == move.type.name:
					damageHit=0
				
		if damageHit > move.damage:
			effectiveText = 'It was super effective.'
		if damageHit < move.damage:
			effectiveText = 'It was not very effective.'
		if damageHit == 0:
			effectiveText = 'It did no damage.'

		defending_pokemon.hp = defending_pokemon.hp - damageHit

	moveText = active_pokemon.name + ' used ' + move.name + '. ' + effectiveText

	if move.moveAction == 'drain':
		active_pokemon.hp = active_pokemon.hp + (damageHit/2)

	if move.moveAction == 'superdrain':
		active_pokemon.hp = active_pokemon.hp + (damageHit*9999999)


	minusCard(cardFrameL)
	minusCard(cardFrameR)
	if active_pokemonL.hp < 0:
		active_pokemonL.hp = 0	
	makeCard(active_pokemonL, cardFrameL)
	if active_pokemonR.hp < 0:	
		active_pokemonR.hp = 0	
	makeCard(active_pokemonR, cardFrameR)

	if defending_pokemon.hp == 0:
		effectiveText = effectiveText + ' ' + defending_pokemon.name + ' fainted.'

	moveText = active_pokemon.name+ ' used ' + move.name + '. ' + effectiveText

	minusCard(headerFrame)
	title = tk.Label(headerFrame, text=moveText, font='Helvetica 14 bold', fg=move.type.color)
	title.pack(side="top")


# Basic function for clearing cards
def minusCard(cardFrame):
	for thing in cardFrame.winfo_children():
		thing.destroy()

def startGame():
	newPoke(cardFrameL)
	newPoke(cardFrameR)
	minusCard(buttonFrame)


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
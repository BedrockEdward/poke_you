import tkinter as tk
from random import randint
from utils import minusCard
# Create an attack button
def attackButton(card, player, move, opponent, benchSpot, game, headerFrame):
	moveButton = tk.Button(card, width=20, fg=move.type.color, text=move.name, font='Helvetica 10 bold',
		command=lambda:moveAttack(player, move, opponent, benchSpot, game, headerFrame))
	moveButton.pack()


# Attack the pokemon by reducing the hp, clearing the cards, and then making them again
def moveAttack(player, move, opponent, benchSpot, game, headerFrame):
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
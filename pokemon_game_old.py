import tkinter as tk
from random import randint


from pokedex import pokemon_list, pokemon


root = tk.Tk()
root.title("pokemon-battle")
root.geometry("1000x700")


headerFrame = tk.Frame(root, width=100)
cardFrameL = tk.Frame(root, width=636,height=200, bg="#ffafff")
cardFrameR = tk.Frame(root, width=636,height=200, bg="#ffafff")
buttonFrameL = tk.Frame(root, width=100)
buttonFrameR = tk.Frame(root, width=100)
playerFrame = tk.Frame(root, width=100)

cardFrameL.pack_propagate(0)
cardFrameR.pack_propagate(0)

active_pokemonR = []
active_pokemonL = []

def newPoke(cardFrame, side_):
	card = tk.Frame(cardFrame, width=100, height=200, highlightbackground="#ffafff", highlightthickness=1, bg="pink")
	card.pack_propagate(0)
	card.pack(side=side_, padx=3)


	
	pokemon_num = randint(0, len(pokemon_list)-1)
	newPokemon = pokemon(pokemon_list[pokemon_num].name, pokemon_list[pokemon_num].hp * 5, pokemon_list[pokemon_num].move1, pokemon_list[pokemon_num].move2, pokemon_list[pokemon_num].move3)
	if cardFrame == cardFrameL:
		active_pokemonL.append(newPokemon)
	if cardFrame == cardFrameR:
		active_pokemonR.append(newPokemon)
		

	if cardFrame == cardFrameL:
		hp = tk.Label(card, text=active_pokemonL[0].hp, width=100, font='Helvetica 20 bold', bg="#ff0fff")
	if cardFrame == cardFrameR:	
		hp = tk.Label(card, text=active_pokemonR[0].hp, width=100, font='Helvetica 20 bold', bg="#ff0fff")

	hp.pack()

	if cardFrame == cardFrameL:
		pokeName = tk.Label(card, text=active_pokemonL[0].name, font='Helvetica 10 bold', bg="#ffafff")
	if cardFrame == cardFrameR:
		pokeName = tk.Label(card, text=active_pokemonR[0].name, font='Helvetica 10 bold', bg="#ffafff")

	pokeName.pack()
	if cardFrame == cardFrameL:
		moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonL[0].move1.name, font='Helvetica 10 bold', command=lambda:moveAttackL(active_pokemonL[0].move1.damage))
	if cardFrame == cardFrameR:
		moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonR[0].move1.name, font='Helvetica 10 bold', command=lambda:moveAttackR(active_pokemonR[0].move1.damage))

	moveButton.pack()

	if cardFrame == cardFrameL:
		moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonL[0].move2.name, font='Helvetica 10 bold', command=lambda:moveAttackL(active_pokemonL[0].move2.damage))
	if cardFrame == cardFrameR:
		moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonR[0].move2.name, font='Helvetica 10 bold', command=lambda:moveAttackR(active_pokemonR[0].move2.damage))

	moveButton.pack()

	if cardFrame == cardFrameL:
		moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonL[0].move3.name, font='Helvetica 10 bold', command=lambda:moveAttackL(active_pokemonL[0].move3.damage))
	if cardFrame == cardFrameR:
		moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonR[0].move3.name, font='Helvetica 10 bold', command=lambda:moveAttackR(active_pokemonR[0].move3.damage))

	moveButton.pack()

def moveAttackR(damage):

	active_pokemonL[0].hp = active_pokemonL[0].hp - damage
	for thing in cardFrameL.winfo_children():
		thing.destroy()
	card = tk.Frame(cardFrameL, width=100, height=200, highlightbackground="#ffafff", highlightthickness=1, bg="pink")
	card.pack_propagate(0)
	card.pack(side='right', padx=3)

	hp = tk.Label(card, text=active_pokemonL[0].hp, width=100, font='Helvetica 20 bold', bg="#ff0fff")
	hp.pack()
	pokeName = tk.Label(card, text=active_pokemonL[0].name, font='Helvetica 10 bold', bg="#ffafff")
	pokeName.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonL[0].move1.name, font='Helvetica 10 bold', command=lambda:moveAttackL(active_pokemonL[0].move1.damage))
	moveButton.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonL[0].move2.name, font='Helvetica 10 bold', command=lambda:moveAttackL(active_pokemonL[0].move2.damage))
	moveButton.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonL[0].move3.name, font='Helvetica 10 bold', command=lambda:moveAttackL(active_pokemonL[0].move3.damage))
	moveButton.pack()

def moveAttackL(damage):

	active_pokemonR[0].hp = active_pokemonR[0].hp - damage
	for thing in cardFrameR.winfo_children():
		thing.destroy()
	card = tk.Frame(cardFrameR, width=100, height=200, highlightbackground="#ffafff", highlightthickness=1, bg="pink")
	card.pack_propagate(0)
	card.pack(side='left', padx=3)

	hp = tk.Label(card, text=active_pokemonR[0].hp, width=100, font='Helvetica 20 bold', bg="#ff0fff")
	hp.pack()
	pokeName = tk.Label(card, text=active_pokemonR[0].name, font='Helvetica 10 bold', bg="#ffafff")
	pokeName.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonR[0].move1.name, font='Helvetica 10 bold', command=lambda:moveAttackR(active_pokemonR[0].move1.damage))
	moveButton.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonR[0].move2.name, font='Helvetica 10 bold', command=lambda:moveAttackR(active_pokemonR[0].move2.damage))
	moveButton.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemonR[0].move3.name, font='Helvetica 10 bold', command=lambda:moveAttackR(active_pokemonR[0].move3.damage))
	moveButton.pack()

## GEORGE: TO DO
def makeCard(active_pokemon, cardFrame, side):
	card = tk.Frame(cardFrame, width=100, height=200, highlightbackground="#ffafff", highlightthickness=1, bg="pink")
	card.pack_propagate(0)
	card.pack(side='left', padx=3)

	hp = tk.Label(card, text=active_pokemon[0].hp, width=100, font='Helvetica 20 bold', bg="#ff0fff")
	hp.pack()
	pokeName = tk.Label(card, text=active_pokemon[0].name, font='Helvetica 10 bold', bg="#ffafff")
	pokeName.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemon[0].move1.name, font='Helvetica 10 bold', command=lambda:moveAttack())
	moveButton.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemon[0].move2.name, font='Helvetica 10 bold', command=lambda:moveAttack())
	moveButton.pack()
	moveButton = tk.Button(card, width=20, fg="#ffafff", text=active_pokemon[0].move3.name, font='Helvetica 10 bold', command=lambda:moveAttack())
	moveButton.pack()

def moveAttack(defending_pokemon, cardFrame, side, damage):
	defending_pokemon[0].hp = defending_pokemon[0].hp - damage
	for thing in cardFrameR.winfo_children():
		thing.destroy()
	makeCard(active_pokemon, defending_pokemon, cardFrame, side)



def minusCard(cardFrame):
	for thing in cardFrame.winfo_children():
		thing.destroy()
	if cardFrame == cardFrameL:
		active_pokemonL.clear()
	if cardFrame == cardFrameR:
		active_pokemonR.clear()


headerFrame.config(bg="#ffafff")
plusButtonR = tk.Button(buttonFrameL, width=5, fg="#ffafff", text="+", font='Helvetica 10 bold', command=lambda: newPoke(cardFrameL, "right"))
plusButtonL = tk.Button(buttonFrameR, width=5, fg="#ffafff", text="+", font='Helvetica 10 bold', command=lambda: newPoke(cardFrameR, "left"))
minusButtonR = tk.Button(buttonFrameL, width=5, fg="#ffafff", text="-", font='Helvetica 10 bold', command=lambda:minusCard(cardFrameL))
minusButtonL = tk.Button(buttonFrameR, width=5, fg="#ffafff", text="-", font='Helvetica 10 bold', command=lambda:minusCard(cardFrameR))



title = tk.Label(headerFrame, text="pokemon-battle", font='Helvetica 18 bold')
title.pack(side="top")
plusButtonL.pack(side="left")
plusButtonR.pack(side="right")

minusButtonL.pack(side="right")
minusButtonR.pack(side="left")






headerFrame.pack(side="top", pady=10)
cardFrameL.pack(side="left", pady=50)
cardFrameR.pack(side="right", pady=50)
playerFrame.pack(side="bottom", pady=10)
buttonFrameL.pack(side="bottom", pady=10)
buttonFrameR.pack(side="bottom", pady=10)












root.mainloop()































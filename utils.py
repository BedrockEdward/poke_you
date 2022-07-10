# Basic function for clearing cards
def minusCard(cardFrame):
	for thing in cardFrame.winfo_children():
		thing.destroy()
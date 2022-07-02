import poketypes

class attackMove:
	def __init__(self, name, type_, moveAction, param1, param2=100, param3=0):
		self.name = name
		self.moveAction = moveAction
		self.type = type_
		self.damage = 0
		self.accuracy = param2
		self.drainDamage = 0

		if moveAction == 'damage':
			self.damage = param1
			self.accuracy = param2
		elif moveAction == 'drain':
			self.damage = param1
			self.accuracy = param2
		elif moveAction == 'superdrain':
			self.damage = param1
			self.accuracy = param2

hydro_pump = attackMove('Hydro Pump', poketypes.waterType, 'damage', 110, 80)
giga_drain = attackMove('Giga Drain', poketypes.grassType, 'drain', 75, 100)
solar_beam = attackMove('Solar Beam', poketypes.grassType, 'damage', 150, 100)
outrage = attackMove('Outrage', poketypes.dragonType, 'damage', 120, 100)
mega_kick = attackMove('Mega Kick', poketypes.normalType, 'damage', 120, 75)
flare_blitz = attackMove('Flare Blitz', poketypes.fireType, 'damage', 120, 100)
heat_crash = attackMove('Heat Crash', poketypes.fireType, 'damage', 150, 100)
last_resort = attackMove('Last Resort', poketypes.normalType, 'damage', 140, 100)
brine = attackMove('Brine', poketypes.waterType, 'damage', 65, 100)
liquidation = attackMove('Liquidation', poketypes.waterType, 'damage', 85, 100)
flip_turn = attackMove('Flip Turn', poketypes.waterType, 'damage', 65, 100)
wild_charge = attackMove('Wild Charge', poketypes.electricType, 'damage', 110, 100)
electro_ball = attackMove('Electro Ball', poketypes.electricType, 'damage', 110, 100)
lava_plume = attackMove('Lava Plume', poketypes.fireType, 'damage', 85, 100)
overheat = attackMove('Overheat', poketypes.fireType, 'damage', 130, 90)
moongeist_beam = attackMove('Moongeist\nBeam', poketypes.psychicType, 'damage', 250, 100)
future_sight = attackMove('Future Sight', poketypes.psychicType, 'damage', 140, 100)
focus_blast = attackMove('Focus Blast', poketypes.fightingType, 'damage', 140, 70)
sunsteal_strike = attackMove('Sunsteal\nStrike', poketypes.steelType, 'damage', 250, 100)
flash_cannon = attackMove('Flash Cannon', poketypes.steelType, 'damage', 110, 100)
gyro_ball = attackMove('Gyro Ball', poketypes.steelType, 'damage', 110, 100) #damage depends on speed
multi_attack = attackMove('Multi-Attack', poketypes.normalType, 'damage', 200, 100)
explosion = attackMove('Explosion', poketypes.normalType, 'damage', 250, 100) #kill user
tri_attack = attackMove('Tri Attack', poketypes.normalType, 'damage', 110, 100)
power_whip = attackMove('Power Whip', poketypes.grassType, 'damage', 120, 85)
leaf_storm = attackMove('Leaf Storm', poketypes.grassType, 'damage', 130, 90)
high_jump_kick = attackMove('High Jump\nKick', poketypes.fightingType, 'damage', 130, 90)
sludge_bomb = attackMove('Sludge Bomb', poketypes.poisonType, 'damage', 95, 100, 100)
petal_blizzard = attackMove('Petal\nBlizzard', poketypes.grassType, 'damage', 110, 100)
blizzard = attackMove('Blizzard', poketypes.iceType, 'damage', 110, 70)
sheer_cold = attackMove('Sheer Cold', poketypes.iceType, 'damage', 999999, 30)
behemoth_bash = attackMove('Behemoth\nBash', poketypes.steelType, 'damage', 250, 100)
behemoth_blade = attackMove('Behemoth\nBlade', poketypes.steelType, 'damage', 250, 100)
scald = attackMove('Scald', poketypes.fireType, 'damage', 80, 100)
draco_meteor = attackMove('Draco\nMeteor', poketypes.dragonType, 'damage', 250, 90)
shadow_ball = attackMove('Shadow Ball', poketypes.ghostType, 'damage', 150, 100)
z_move = attackMove('Z-Move', poketypes.normalType, 'damage', 250, 100)
dark_pulse = attackMove('Dark Pulse', poketypes.darkType, 'damage', 110, 100)
dazzling_gleam = attackMove('Dazzling\nGleam', poketypes.fairyType, 'damage', 110, 100)
iron_tail = attackMove('Iron Tail', poketypes.steelType, 'damage', 110, 75)
drain_kiss = attackMove('Drain Kiss', poketypes.fairyType, 'drain', 110, 100)

jungle_healing = attackMove('Jungle Healing', poketypes.grassType, 'drain', 200, 100)
throat_chop = attackMove('Throat Chop', poketypes.darkType, 'damage', 250, 100)
close_combat = attackMove('Close Combat', poketypes.fightingType, 'damage', 120, 100)
foul_play = attackMove('Foul Play', poketypes.darkType, 'damage', 150, 100)
psychic = attackMove('Psychic', poketypes.psychicType, 'damage', 200, 100)
mew_move = attackMove('Mew Move', poketypes.psychicType, 'damage', 999999, 60)
mewtwo_move = attackMove('Mewtwo Move', poketypes.psychicType, 'damage', 999999, 60)
zap_cannon = attackMove('Zap Cannon', poketypes.electricType, 'damage', 250, 100)
electric = attackMove('Electric', poketypes.fairyType, 'damage', 400, 70)
electric2 = attackMove('Electric2', poketypes.darkType, 'damage', 400, 70)
electric3 = attackMove('Electric3', poketypes.steelType, 'damage', 400, 70)
ice = attackMove('Ice', poketypes.fireType, 'damage', 400, 70)
ice2 = attackMove('Ice2', poketypes.iceType, 'damage', 400, 70)
ice3 = attackMove('Ice3', poketypes.fightingType, 'damage', 400, 70)
fire = attackMove('Fire', poketypes.psychicType, 'damage', 400, 70)
fire2 = attackMove('Fire2', poketypes.fightingType, 'damage', 400, 70)
fire3 = attackMove('Fire3', poketypes.bugType, 'damage', 400, 70)
revive = attackMove('Revive', poketypes.loveType, 'superdrain', 1, 100)
love = attackMove('Love', poketypes.loveType, 'damage', 9999999, 10)
kill = attackMove('Kill', poketypes.loveType, 'damage', 9999999, 50)





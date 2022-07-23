import movelist as move
import poketypes
from random import randint, choice 
class pokemon:
	def __init__(self, name, type_, type2_, hp, movelist):
		self.name = name
		self.type = type_
		self.type2 = type2_
		self.hp = hp
		self.movelist = movelist
		self.move1 = choice(movelist)
		self.move2 = choice(movelist)
		self.move3 = choice(movelist)
		self.move4 = choice(movelist)


pokemon_list = [
	pokemon("Blastoise", poketypes.waterType, None, 186, [move.hydro_pump, move.mega_kick, move.scald]),
	pokemon("Venusaur", poketypes.grassType, poketypes.poisonType, 187, [move.petal_blizzard, move.solar_beam, move.power_whip]),
	pokemon("Charizard", poketypes.fireType, poketypes.flyingType, 185, [move.overheat, move.heat_crash, move.flare_blitz]),
	pokemon("Sylveon", poketypes.fairyType, None, 202, [move.last_resort, move.drain_kiss, move.dazzling_gleam]),
	pokemon("Umbreon", poketypes.darkType, None, 202, [move.last_resort, move.shadow_ball, move.dark_pulse]),
	pokemon("Jolteon", poketypes.electricType, None, 172, [move.last_resort, move.wild_charge, move.shadow_ball]),
	pokemon("Flareon", poketypes.fireType, None, 172, [move.overheat, move.heat_crash, move.flare_blitz]),
	pokemon("Vaporeon", poketypes.waterType, None, 202, [move.blizzard, move.flip_turn, move.hydro_pump]),
	pokemon("Glaceon", poketypes.iceType, None, 172,  [move.sheer_cold, move.blizzard, move.shadow_ball]),
	pokemon("Leafeon", poketypes.grassType, None, 172, [move.leaf_storm, move.solar_beam, move.giga_drain]),
	pokemon("Espeon", poketypes.psychicType, None, 172, [move.future_sight, move.last_resort, move.shadow_ball]),
	pokemon("Tsareena", poketypes.grassType, poketypes.fairyType, 179, [move.leaf_storm, move.high_jump_kick, move.giga_drain]),
	pokemon("Zamazenta", poketypes.fightingType, poketypes.steelType, 244, [move.behemoth_bash, move.behemoth_blade, move.gyro_ball]),
	pokemon("Zacian", poketypes.fairyType, poketypes.steelType, 244, [move.behemoth_blade, move.behemoth_bash, move.gyro_ball]),
	pokemon("Milotic", poketypes.waterType, None, 202, [move.scald, move.hydro_pump, move.flip_turn]),
	pokemon("Silvally", poketypes.normalType, None, 202, [move.draco_meteor, move.explosion, move.multi_attack]),
	pokemon("Gengar", poketypes.ghostType,  poketypes.poisonType, 200, [move.shadow_ball, move.mega_kick, move.dark_pulse]),
	pokemon("Lunala", poketypes.psychicType,  poketypes.ghostType, 244, [move.z_move, move.moongeist_beam, move.sunsteal_strike]),
	pokemon("Solgaleo", poketypes.steelType, poketypes.psychicType, 244, [move.z_move, move.sunsteal_strike, move.moongeist_beam]),
	pokemon("Mew", poketypes.psychicType, None, 500, [move.psychic, move.behemoth_blade, move.mew_move]),
	pokemon("Mewtwo", poketypes.psychicType, None, 500, [move.foul_play, move.psychic, move.mewtwo_move]),
	pokemon("Zarude", poketypes.darkType, poketypes.grassType, 212, [move.jungle_healing, move.throat_chop, move.close_combat]),
	pokemon("Zapdos", poketypes.electricType, poketypes.flyingType, 500, [move.zap_cannon, move.electric, move.electric2]),
	pokemon("G. Zapdos", poketypes.fightingType, poketypes.flyingType, 500, [move.electric, move.electric2, move.electric3]),
	pokemon("Articuno", poketypes.iceType, poketypes.flyingType, 500, [move.blizzard, move.ice, move.ice2]),
	pokemon("G. Articuno", poketypes.psychicType, poketypes.flyingType, 500, [move.ice, move.ice2, move.ice3]),
	pokemon("Moltres", poketypes.fireType, poketypes.flyingType, 500, [move.overheat, move.fire, move.fire2]),
	pokemon("G. Moltres", poketypes.darkType, poketypes.flyingType, 500, [move.fire, move.fire2, move.fire3]),
	pokemon("Arceus", poketypes.loveType, None, 9999999, [move.love, move.kill, move.revive, move.wtf])
























































]


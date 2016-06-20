class WarBand(object):
	def __init__(self, warband_name, heroes, henchmen, weapons, armor, spells, items):
		self.warband_name = warband_name
		self.heroes = heroes
		self.henchmen = henchmen
		self.weapons = weapons
		self.armor = armor
		self.spells = spells
		self.items = items

warband_name = raw_input('Which warband do you wish to play as?').strip()

def tutorial():
	help = raw_input("If you need assistance, please type 'help'. Otherwise we will move on to warband creation").strip()
	for answer in help:
		if warband_name == 'sisters of sigmar'.lower() and help == 'help'.lower():
			answer = raw_input("What do you want to know about? Please enter heroes, henchmen, weapons, equiptment, or spells. To exit this tutorial, please type 'exit'").strip()
			if answer == 'heroes'.lower():
				heroes = open('sigmarite heroes.txt')
				print heroes.read()
				heroes.close()
			elif answer == 'henchmen'.lower():
				henchmen = open('sigmarite henchmen.txt')
				print henchmen.read()
				henchmen.close()	
			elif answer == 'weapons':
				weapons = open('sigmarite weapons'.txt)
				print weapons.read()
				weapons.close()
			elif answer == 'equiptment':
				equiptment = open('sigmarite equiptment.txt')
				print equiptment.read()
				equiptment.closer()
			elif answer == 'spells':
				spells = open('sigmarite spells.txt')
				print spells.read()
				spells.close()
			else:
				break

tutorial()

#Classes to hold all the warband related data. 

class Stats(object):
	def __init__(self, movement, weapon_skill, ballistic_skill, strength, toughness, w, initiative, attack, leadership):
		self.movement = movement
		self.weapon_skill = weapon_skill
		self.ballistic_skill = ballistic_skill
		self.strength = strength
		self.toughness = toughness
		self.w = w 
		self.initiative = initiative
		self.attack = attack
		self.leadership = leadership 

matriarch_stats = Stats(4,4,4,3,3,1,4,1,8)
superior_stats = Stats(4,4,3,3,3,1,3,1,7)
augur_stats = Stats(4,2,2,3,3,1,3,1,7)
sister_stats = Stats(4,3,3,3,3,1,3,1,7)
novice_stats = Stats(4,2,2,3,3,1,3,1,6)

class Character(object):
	def __init__(self, character_type, character_name, description, weapons_armor, special_rules, experience, cost, units,stats):
		self.character_type = character_type
		self.character_name = character_name
		self.description = description
		self.weapons_armor = weapons_armor
		self.special_rules = special_rules
		self.experience = experience
		self.cost = cost
		self.units = units
		self.stats = stats

sigmarite_matriarch = Character('hero','Sigmarite Matriarch','The Sigmarite Matriarchs, of whom there is an inner circle of twelve, are answerable to the High Matriarch of the temple. Each must lead a warband of Sisters in frequent searches of the city in order to purge the ruins. Matriarchs are driven by a zealous devotion to the Cult of Sigmar and a relentless determination to redeem the Sisterhood in His eyes.', 'The Sigmarite Matriarch may be equipped with weapons and armour chosen from the Sisters of Sigmar Equipment list.','Leader: Any warband member within 6" of the Sigmarite Matriarch may use her Leadership characteristic when taking any Leadership tests', 20, 75, 1, matriarch_stats)

sister_superior = Character('hero','Sister Superior', 'Each of the Sisters Superior is a long-serving priestess of the Cult of Sigmar, well versed in the rituals of the temple and an example to the younger Sisters and Novices. The Sisters Superior are entrusted with maintaining the faith and fervour of the order. Any peril or foe that may lurk in the ruins of Mordheim is as nothing compared to the wrath of a Sister Superior.', 'A Sister Superior may be equipped with weapons and armour chosen from the Sisters of Sigmar Equipment list.','No special rules', 8, 35,3,superior_stats)

augur = Character('hero','augur', 'The blind Augurs of the Sisterhood are blessed beyond their comrades. By giving up their sight they have gained something far more, second sight - a gift from their patron god. Only a very few are marked this way, and they are greatly revered by the Sisterhood. Unlike the rest of the priestesses, they shave their heads, save for a single long braid.','The Augurs may be equipped with weapons chosen from the Sisters of Sigmar Equipment list. They never wear armour.','Blessed Sight: An Augur can re-roll any failed characteristic tests (climbing, resisting spells or any other reason), and any rolls to hit in close combat or shooting. You must accept the second result. In addition, an Augur can use her Blessed Sight to help the Sisterhood when they are searching the city for wyrdstone. If the Augur is not put out of action in the battle, you may roll two dice for her in the exploration phase and pick either dice as the result.',0,25,1,augur_stats)

sigmarite_sister = Character('henchman', 'sigmarite sister', 'Sigmarite Sisters know that their entire order is shamed in the eyes of their Lord Sigmar. Every one of them is sworn upon His altar to pacify the city and thereby redeem themselves. Whatever the perils and horrors that stand in their way, they will be overcome!', 'The Sigmarite Sisters may be equipped with weapons and armour chosen from the Sisters of Sigmar Equipment list.', 'No special rules', 0, 25, 'no limit to number of sisters', sister_stats)

novice = Character('henchman','novice', 'By tradition, the Sisters draw their recruits only from the most noble houses of the Empire, and families consider it a great honour to have their daughter accepted into the order. Only maidens of noble lineage can be relied upon to have the devotion to duty and innate sense of honour. Few though the recruits may be, they must endure several years as Novices during which time their devotion will be tested to the full. All are eager to prove themselves worthy to be the handmaidens of Sigmar.', 'The Novices may be equipped with weapons and armour chosen from the Sisters of Sigmar Equipment list.', 'No special rules', 0, 15, 10, novice_stats)

class Weapons(object):
	def __init__(self, weapon_name, description, weapon_range, strength, special_rules, cost):
		self.weapon_name = weapon_name
		self.description = description
		self.weapon_range = weapon_range
		self.strength = strength
		self.special_rules = special_rules
		self.cost = cost

dagger = Weapons('dagger','Daggers and knives are extremely common, and men are allowed to carry them in enclaves where weapons are otherwise forbidden. Many a warrior in Mordheim has died with a dagger in his back.', 'close combat', 'as user', "+1 Enemy armour save: Daggers are not the best weapons to use for penetrating an enemy model's armour. An enemy wounded by a dagger gains a +1 bonus to his armour save, and a 6+ armour save if he has none normally.", 2)

mace = Weapons('mace', 'Perhaps the simplest type of weapon, these brutal, bludgeoning instruments range from primitive wooden clubs to elaborately forged Dwarf hammers made from the finest steel. A blow from a mace can easily crush a skull or knock a man unconscious','close combat','as user', "Concussion: Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model's injuries.", 3)

hammer = Weapons('hammer','Perhaps the simplest type of weapon, these brutal, bludgeoning instruments range from primitive wooden clubs to elaborately forged Dwarf hammers made from the finest steel. A blow from a mace can easily crush a skull or knock a man unconscious','close combat','as user', "Concussion: Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model's injuries.", 3)

sigmarite_warhammer = Weapons('sigmarite warhammer', 'One of the traditional weapons of the Sisterhood, the warhammer echoes Ghal-Maraz,the great hammer of Sigmar himself', 'close combat', 'as user +1', 'Concussion: Warhammers are excellent at striking people senseless. When using a warhammer in close combat a roll of 2-4 is treated as stunned when rolling on the Injury chart.\nHoly Weapon: Each warhammer is blessed by the High Matriarch herself before it is handed to the Sisters. The warhammer has a +1 bonus on all to wound rolls against any Possessed or Undead models. Note that you will still need to score a 6 before any modifiers in order to cause a critical hit. Only Matriarchs and Sister Superiors may carry two Sigmarite warhammers.', 15)

steel_whip = Weapons('steel whip', "Another weapon unique to the Sisterhood is the steel whip, made from barbed steel chains. The weapon can be as much as 12' long and some of the Sisters have acquired a truly punishing skill with this weapon.", '4"', 'as user', 'Cannot be parried: The steel whip is a flexible weapon and the Priestesses use it with great expertise. Attempts to parry its strikes are futile. A model attacked by a steel whip may not make parries with swords or bucklers.\nReach: A model armed with a steel whip may attack enemies up to 4" away in the hand-to-hand combat phase. She may make her usual number of attacks, using the normal combat procedure, except that her opponent may not strike back. Note that if the model is already engaged in close combat, she may not use the steel whip to attack opponents other than those in base contact.', 10)

flail = Weapons('flail', "The flail is a heavy weapon wielded with both hands. It normally consists of heavy weights, often spiked, attached to a pole or handle by means of heavy chains. Flails drain the user's stamina quickly, but are awesomely destructive in the hands of a skilled (or unhinged) warrior.", 'close combat', 'as user +2', 'Heavy: A flail is extremely tiring to use and thus the +2 Strength bonus applies only in the first turn of each hand-to-hand combat.\nTwo-handed: As a flail requires two hands to use, a model using a flail may not use a shield, buckler or additional weapon in close combat. If the model has a shield he still gets a +1 bonus to his armour save against shooting.',15)

double_handed_weapon = Weapons('double handed weapon', 'A blow from a double-handed axe or sword can cut a foe in half and break armour apart. It takes a long time to learn how to use these weapons and even then only extremely strong men are able to wield them effectively', 'close combat', 'as user +2', 'Two-handed: A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armour save against shooting.\nStrike last: Double-handed weapons are so heavy that the model using them always strikes last, even when charging.', 15)

sling = Weapons('sling', "Slings are rarely used, mainly because they are no more powerful than bows and have a shorter range. A sling is little more than a looped strip of cloth or leather into which a stone is placed. The sling is whirled about the slinger's head and the sling stone is then released towards the target. While this weapon is looked down upon by most archers, a skilled slinger can slay a man from a considerable distance, and the ammunition is easy to find: rocks are everywhere and free!", '18"', 3, 'Fire twice at half range: A slinger may fire twice in the shooting phase if he does not move in the movement phase. He cannot shoot over half range (9") though, if he fires twice.', 2)

class Armour(object):
	def __init__(self, armour_name, description, saving_throw, movement, cost):
		self.armour_name = armour_name
		self.description = description
		self.saving_throw = saving_throw
		self.movement = movement
		self.cost = cost

light_armour = Armour('light armour', 'Light armour encompasses a wide variety of materials from hardened leather tunics to chain shirts forged from steel. It does not offer complete protection against arrows or swords, but it is better than having nothing at all.', 'A warrior who is wearing light armour has a basic D6 saving throw of 6.', 'Light armour does not inhibit movement.', 20)

heavy_armour = Armour('heavy armour', 'Typical heavy armour is made from metal links and is called chain mail. Forging chain mail is a laborious and time consuming process, as the blacksmith must put together hundreds, sometimes thousands, of metal links. This makes chain mail expensive, but this type of armour provides excellent protection for anyone who can afford it. There are other types of heavy armour as well, of which the best known are the steel breastplates and greaves worn by the foot knights of the Templar orders.', 'A warrior that is wearing heavy armour has a basic D6 saving throw of 5+.', 'A warrior that is armed with both heavy armour and a shield suffers a -1 Movement penalty.', 50)

shield = Armour('shield', "There are two types of shield common to the warriors of Mordheim: the first is made of wood, occasionally reinforced with metal plates. This basic type of shield, although strong, does tend to splinter, but this can sometimes save the user's life as his enemy's weapon can get trapped allowing him to strike back whilst his enemy struggles to free his weapon. Metal shields are heavy and cumbersome, but last much longer and can take a battering. A typical Empire shield is either round or triangular, and carries the emblem of the province or city of its owner.", ' A model with a shield has a basic save of 6 on a D6', 'Shields do not inhibit movement.', 5)

buckler = Armour('buckler', 'Bucklers are small, round shields designed for parrying or deflecting blows.They are usually made of steel for they need to be tremendously durable to survive the brutal blows of hand-to-hand combat. Using a buckler requires great skill, but a nimble warrior can protect himself from blows which would otherwise cripple him.', 'Parry: A model equipped with a buckler may parry the first blow in each round of hand-to-hand combat. When his opponent scores a hit, a model with a buckler may roll 1D6. If the score is greater than the highest to hit score of his opponent, the model has parried the blow, and that attack is discarded. A model may not parry attacks made with double or more its own Strength - they are simply too powerful to be stopped.', 'Buckers do not inhibit movement.', 5)

helmet = Armour('helmet', 'From the shining steel helmets of Bretonnian knights to the leather caps of the Skaven, all sensible warriors try to protect the most vulnerable part of their body - their head. Even the most vain fighters still use a helmet, as it can be festooned with plumes, horns and other decorations. Helmets come in varying shapes and sizes, but their basic function remains the same.', "A model that is equipped with a helmet has a special 4+ save on a D6 against being stunned. If the save is made, treat the stunned result as knocked down instead. This save is not modified by the opponent's Strength.", 'Helmets do not inhibit movement', 10)

class MiscellaneousEquipment(object):
	def __init__(self, item_name, description, use, cost):
		self.item_name = item_name
		self.description = description
		self.use = use
		self.cost = cost

holy_tome = MiscellaneousEquipment('holy tome', "Books of prayers and descriptions of the holy deeds of religious heroes like Sigmar Heldenhammer are copied by hand in the scriptoriums of Sigmar and Ulric, and given or sold to the faithful. Of these tomes, the Deus Sigmar is the most common and well known, but other texts such as the Scriptures of Sigmar are also sold to those who follow the faith. A holy man can recite his prayers from such a book, strengthening his faith and belief", "A Warrior Priest or Sister of Sigmar with a holy tome can add +1 to the score when determining whether he (or she) can recite a spell successfully or not.", 120)

blessed_water = MiscellaneousEquipment('blessed water', 'The priests of Ulric, Sigmar, Morr and Manann hold great power over evil. Pure water from a clear fountain, blessed by one of these priests, is said to burn things of darkness and evil.', "A vial of blessed water contains enough liquid for just one use, and has a thrown range of twice the thrower's Strength in inches. Roll to hit using the model's BS. No modifiers for range or moving apply. Blessed water causes 1 wound on Undead, Daemon or Possessed models automatically. There is no armour save. Undead or Possessed models may not use blessed water", 10)

holy_relic = MiscellaneousEquipment('holy relic', "In this age of superstition and religious fanaticism, holy objects are an important part of life. Relics abound in the Old World: hairs of Sigmar, pieces from Ulric's hammer, teeth of Daemon Princes, all are sold to men needing encouragement before battle and as charms against sorcery.", "A model with a holy relic will automatically pass the first Leadership test he is required to make in the game. If worn by the leader, it will allow him to automatically pass the first Rout test if he has not taken any Leadership tests before. You can only ignore the first Leadership test in any single game - owning two or more holy relics will not allow you to ignore second and subsequent tests.", 15)

class Spells(object):
	def __init__(self, spell_name, description, difficulty, use):
		self.spell_name = spell_name
		self.description = description
		self.difficulty = difficulty
		self.use = use

hammer_of_sigmar = Spells('The Hammer of Sigmar', 'This weapon of the faithful glows with a golden light, imbued as it is with the righteous power of Sigmar.', 7, 'The wielder gains +2 Strength in hand-to-hand combat and all hits he inflicts cause double damage (eg, 2 wounds instead of 1). The Priest must test each shooting phase he wants to use the Hammer.')

hearts_of_steel = Spells('Hearts of Steel', "As the three words of power are spoken, waves of glory surround the servant of Sigmar. The faithful are heartened by the warrior god's presence.", 8, 'Any allied warriors within 8" of the warrior become immune to Fear and All Alone tests. In addition, the whole warband gains +1 to any Rout tests they have to make. The effects of this spell last until the caster is knocked down, stunned or put out of action. If cast again the effects are not cumulative, ie, the maximum bonus to Rout tests remains +1.')

soulfire = Spells('SoulFire', 'The wrath of Sigmar comes to earth. Purifying flames surround the Priest and wipe out those who resist the righteous fury of the God-Emperor!', 9, "All enemy models within 4 inches of the servant of Sigmar suffer a Strength 3 hit. No armour saves are allowed. The servants of darkness and Chaos are especially susceptible to Sigmar's holy power. Undead and Possessed models in range suffer a Strength 5 hit instead.")

shield_of_faith = Spells('Shield of Faith', 'A shield of pure white light appears in front of the Priest. As long as his faith remains strong the shield will protect him.', 6, 'The Priest is immune to all spells. Roll at the beginning of each turn in the recovery phase. On a roll of 1 or 2 the shield disappears')

healing_hand = Spells('Healing Hand', "Laying hands upon a wounded comrade, the servant of Sigmar calls upon his Lord to heal the warrior's wounds", 5, 'Any one model within 2" of the Priest (including himself) may be healed. The warrior is restored to his full quota of Wounds. In addition, if any friendly models within 2" are stunned or knocked down, they immediately come to their senses, stand up, and continue fighting as normal.')

armour_of_righteousness = Spells('Armour of Righteousness', 'Impenetrable armour covers the Priest and the fiery image of a twin-tailed comet burns above his head.', 9, "The Priest has an armour save of 2+ which replaces his normal armour save. In addition, he causes fear in his enemies and is therefore immune to fear himself. The power of the Armour of Righteousness lasts until the beginning of the Priest's next Shooting phase.")


class WarBand(object):
	def __init__(self, warband_name, heroes, henchmen, weapons, armor, spells):
		self.warband_name = warband_name
		self.heroes = heroes
		self.henchmen = henchmen
		self.weapons = weapons
		self.armor = armor
		self.spells = spells




# assigning the classes to specific variables 


#Call the entire warband object

# 'Experience':20, 'Cost':75, 'Units':1, 'stats': {'movement':4, 'weapon skill':4, 'ballistic skill':4, 'strength':3, 'toughness':3, 'w':1, 'initiative':4, 'attack':1, 'leadership':8}}

# my_character = Character(heroes='my big list of heroes', stats=1)




# print sisters_of_sigmar.heroes

# warband_name = raw_input('Which warband do you wish to play as?').strip()

# help = raw_input("If you need assistance, please type 'help'. To move on to warband creation, please type 'move on'").strip()

# def tutorial():
# 	if help == 'help':
# 		for answer in help:
# 			if warband_name == 'sisters of sigmar'.lower() and help == 'help'.lower():
# 				answer = raw_input("What do you want to know about? Please enter heroes, henchmen, weapons, equiptment, or spells. To exit this tutorial, please type 'exit'").strip()
# 			if answer == 'heroes'.lower():
# 				heroes = open('sigmarite heroes.txt')
# 				print heroes.read()
# 				heroes.close()
# 			elif answer == 'henchmen'.lower():
# 				henchmen = open('sigmarite henchmen.txt')
# 				print henchmen.read()
# 				henchmen.close()	
# 			elif answer == 'weapons':
# 				weapons = open('sigmarite weapons.txt')
# 				print weapons.read()
# 				weapons.close()
# 			elif answer == 'equiptment':
# 				equiptment = open('sigmarite equiptment.txt')
# 				print equiptment.read()
# 				equiptment.closer()
# 			elif answer == 'spells':
# 				spells = open('sigmarite spells.txt')
# 				print spells.read()
# 				spells.close()
# 			else:
# 				break

# tutorial()

# def warband_creation():
# 	if help == 'move on':
# 		user_heroes = raw_input('Which heroes would you like to select? Your options are: %s' % (sisters_of_sigmar.heroes.keys()))



# warband_creation()
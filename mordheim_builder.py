# start with 1 warband  then go to 2 warband
# if you go to 2 warband, ask the user which warband they want to play




def band_choice():
	warband = raw_input('Which warband would you like to play? ')
	#for answers in details:
	if warband =="Sisters of Sigmar".lower():
		details = raw_input("If you would like to know more about characters, type 'Characters'.\nIf you would like to know  more about weapons and equipment, type 'Weapons'.\nIf you would like to know more about Prayers of Sigmar, please type 'Magic'. If you would like to move on to character creation, please type 'Move on.'")
		if details.lower() == 'characters':
			info = raw_input('Who would you like to know more about? Please enter one of the following: sigmar matriarch, sister superior, augur, sigmarite sister, or novice. If you would like to move on, please enter: move on: ')
			if info.lower() == 'sigmar matriarch':
				matriarch = raw_input('The Sigmarite Matriarchs, of whom there is an inner circle of twelve, are answerable to the High Matriarch of the temple. Each must lead a warband of Sisters in frequent searches of the city in order to purge the ruins. Matriarchs are driven by a zealous devotion to the Cult of Sigmar and a relentless determination to redeem the Sisterhood in His eyes.\nWeapons/Armour: The Sigmarite Matriarch may be equipped with weapons and armour chosen from the Sisters of Sigmar Equipment list.\nSPECIAL RULES Leader: Any warband member within 6" of the Sigmarite Matriarch may use her Leadership characteristic when taking any Leadership tests.\n They have experience 20 and cost 75 gold\n You may only have one matriarch.\n To learn more about the weapons available, please type: weapons\nPrayers of Sigmar: The Matriarch has studied the Prayers of Sigmar. See the Magic section.\n To learn more about the weapons available, please type: weapons. Otherwise type: n ')
			elif info.lower() == 'sister superior':
				superior = raw_input('Each of the Sisters Superior is a long-serving priestess of the Cult of Sigmar, well versed in the rituals of the temple and an example to the younger Sisters and Novices. The Sisters Superior are entrusted with maintaining the faith and fervour of the order. Any peril or foe that may lurk in the ruins of Mordheim is as nothing compared to the wrath of a Sister Superior.\n Weapons/Armour: A Sister Superior may be equipped with weapons and armour chosen from the Sisters of Sigmar Equipment list.\n They have experience 8 and cost 35 gold. \n You are allowed to have up to 3 sister superiors.\n To learn more about the weapons available, please type: weapons. Otherwise type n')
			elif info.lower() == 'augur':
				augur = raw_input('The blind Augurs of the Sisterhood are blessed beyond their comrades. By giving up their sight they have gained something far more, second sight - a gift from their patron god. Only a very few are marked this way, and they are greatly revered by the Sisterhood. Unlike the rest of the priestesses, they shave their heads, save for a single long braid.\nWeapons/Armour: The Augurs may be equipped with weapons chosen from the Sisters of Sigmar Equipment list. They never wear armour.\nlSPECIAL RULES Blessed Sight: An Augur can re-roll any failed characteristic tests (climbing, resisting spells or any other reason), and any rolls to hit in close combat or shooting. You must accept the second result. In addition, an Augur can use her Blessed Sight to help the Sisterhood when they are searching the city for wyrdstone. If the Augur is not put out of action in the battle, you may roll two dice for her in the exploration phase and pick either dice as the result.\nThey have experience 0 and cost 25 gold.\nYou are allowed to have only one Augur.\n To learn more about weapons available, please type: weapons. Otherwise type n')
			elif info.lower() == 'sigmarite sister':
				sister = raw_input('Sigmarite Sisters know that their entire order is shamed in the eyes of their Lord Sigmar. Every one of them is sworn upon His altar to pacify the city and thereby redeem themselves. Whatever the perils and horrors that stand in their way, they will be overcome!\nWeapons/Armour: The Sigmarite Sisters may be equipped with weapons and armour chosen from the Sisters of Sigmar Equipment list.\nThey have experience 0 and cost 25 gold.')
			elif info.lower() == 'novice':
				novice = raw_input('By tradition, the Sisters draw their recruits only from the most noble houses of the Empire, and families consider it a great honour to have their daughter accepted into the order. Only maidens of noble lineage can be relied upon to have the devotion to duty and innate sense of honour. Few though the recruits may be, they must endure several years as Novices during which time their devotion will be tested to the full. All are eager to prove themselves worthy to be the handmaidens of Sigmar.\nWeapons/Armour: The Novices may be equipped with weapons and armour chosen from the Sisters of Sigmar Equipment list.\n They have experience 0 and cost 15 gold.')
		#elif details.lower() == 'weapons':
		#	weapons = raw_input('Which weapons or armour would you like to know more about? Please type one of the following: sigmarite warhammer, steel whip, dagger, mace, hammer, flail, double-handed weapon, sling, light armour, heavy armour, shield, buckler, helmet, holy tome, blessed water, holy relic.')
		#	if weapons.lower() == 'sigmarite warhammer':
		#		sigmarite warhammer = raw_input('Availability: Common, Sisters of Sigmar only. One of the traditional weapons of the Sisterhood, the warhammer echoes Ghal-Maraz, the great hammer of Sigmar himself.\nSPECIAL RULES Concussion: Warhammers are excellent at striking people senseless. When using a warhammer in close combat a roll of 2-4 is treated as stunned when rolling on the Injury chart. Holy Weapon: Each warhammer is blessed by the High Matriarch herself before it is handed to the Sisters. The warhammer has a +1 bonus on all to wound rolls against any Possessed or Undead models. Note that you will still need to score a 6 before any modifiers in order to cause a critical hit. Only Matriarchs and Sister Superiors may carry two Sigmarite warhammers.\n Cost is 15 gold.')
			#elif weapons.lower() == 'steel whip'



band_choice()






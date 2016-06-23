# need to access the mordheim_classes file
import mordheim_classes

#user input for warband type. Necessary when there are more warbands to choose from.
warband_name = raw_input('Which warband do you wish to play as?').strip()

# start of the tutorial. Gives user option to seek help or move on. 

help = raw_input("If you  need assistance, please type 'help'. To move on to warband creation, please type 'move on'").strip()

#This is a warband tutorial. It allows the user to ask questions regarding specific things relating to Sisters of Sigmar

def tutorial():
    if help == 'help':
        while True:
            if warband_name == 'sisters of sigmar'.lower() and help == 'help'.lower():
                answer = raw_input("\nWhat do you want to know about? Please enter heroes, henchmen, weapons, armour, items, or spells. To exit this tutorial, please type 'move on'").strip()
            if answer == 'heroes'.lower():
                print '\nThe leader is the Sigmarite Matriarch. %s' % mordheim_classes.sigmarite_matriarch.description
                print "\n----------------------"
                print '\nYou also have the Sister Superiors. %s' % mordheim_classes.sister_superior.description,
                print '\n______________________'
                print '\nLastly, you have your Augur %s' % mordheim_classes.augur.description,
            elif answer == 'henchmen'.lower():
                print '\nSigmarite Sisters: %s' % mordheim_classes.sigmarite_sister.description,
                print "\n----------------------"
                print '\nNovices: %s' % mordheim_classes.novice.description,
                print "\n----------------------"
            elif answer == 'weapons':
                print '\nThe dagger: %s' % mordheim_classes.dagger.description
                print "\n----------------------"
                print '\nThe mace: %s' % mordheim_classes.mace.description
                print "\n----------------------"
                print '\nThe hammer: %s' % mordheim_classes.hammer.description
                print "\n----------------------"
                print '\nThe flail: %s' % mordheim_classes.flail.description
                print "\n----------------------"
                print '\nThe double handed weapon: %s' % mordheim_classes.double_handed_weapon.description
                print "\n----------------------"
                print '\nThe sling: %s' % mordheim_classes.sling.description
                print "\n----------------------"
                print '\nThe sisters have two special weapons: the Sigmarite Warhammer and the Steel Whip.\nThe Sigmarite Warhammer is %s.\nThe Steel Whip is %s' % (mordheim_classes.sigmarite_warhammer.description, mordheim_classes.steel_whip.description)
            elif answer == 'armour':
                print '\nLight armour: %s'% mordheim_classes.light_armour.description
                print "\n----------------------"
                print '\nHeavy armour: %s' % mordheim_classes.heavy_armour.description
                print "\n----------------------"
                print '\nShield: %s' % mordheim_classes.shield.description
                print "\n----------------------"
                print '\nBuckler: %s' % mordheim_classes.buckler.description
                print "\n----------------------"
                print '\nHelmet: %s' % mordheim_classes.helmet.description
            elif answer == 'items':
                print '\nHoly Tome: %s' % mordheim_classes.holy_tome.description
                print "\n----------------------"
                print '\nBlessed water: %s' % mordheim_classes.blessed_water.description
                print "\n----------------------"
                print '\nHoly relic: %s' % mordheim_classes.holy_relic.description
            elif answer == 'spells':
                print '\nHammer of Sigmar: %s' % mordheim_classes.hammer_of_sigmar.description
                print "\n----------------------"
                print '\nHeart of Steel: %s' % mordheim_classes.hearts_of_steel.description
                print "\n----------------------"
                print '\nSoulFire: %s' % mordheim_classes.soulfire.description
                print "\n----------------------"
                print '\nShield of Faith: %s' % mordheim_classes.shield_of_faith.description
                print "\n----------------------"
                print '\nHealing Hand: %s' % mordheim_classes.healing_hand.description
                print "\n----------------------"
                print '\nArmour of Righteousness: %s' % mordheim_classes.armour_of_righteousness.description
            else:
                break

tutorial()


if __name__ == '__main__':
    main()

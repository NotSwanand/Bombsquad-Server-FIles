from bsSpaz import *


# cyborg ###################################
t = Appearance("Random")
t.colorTexture = "levelIcon"
t.colorMaskTexture = "null"
t.defaultColor = (0.5,0.5,0.5)
t.defaultHighlight = (random.random()*2,random.random()*2,random.random()*2)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  random.choice(["cyborgForeArm", 'zoeForeArm'])
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1','cyborg2','cyborg3','cyborg4']
cyborgHitSounds = ['cyborgHit1','cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'pixie'

# cyborg ###################################
t = Appearance("TG")
t.colorTexture = "tipTopLevelColor"
t.colorMaskTexture = "cyborgColorMask"
t.defaultColor = (0.5,0.5,0.5)
t.defaultHighlight = (1,0,0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1','cyborg2','cyborg3','cyborg4']
cyborgHitSounds = ['cyborgHit1','cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# Cowboy ###################################
t = Appearance("Special")
t.colorTexture = "crossOut"
t.colorMaskTexture = "crossOut"
t.defaultColor = (0.3,0.5,0.8)
t.defaultHighlight = (1,0,0)
t.iconTexture = "logo"
t.iconMaskTexture = "logoEaster"
t.headModel =     "agentHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cowboyUpperArm"
t.foreArmModel =  "cowboyForeArm"
t.handModel =     "cowboyHand"
t.upperLegModel = "cowboyUpperLeg"
t.lowerLegModel = "cowboyLowerLeg"
t.toesModel =     "cyborgToes"
cowboySounds =    ['wizard1','wizard2','wizard3','wizard4']
cowboyHitSounds = ['cyborgHit1','cyborgHit2']
t.attackSounds = cowboySounds
t.jumpSounds = cowboySounds
t.impactSounds = cowboyHitSounds
t.deathSounds=["bonesDeath"]
t.pickupSounds = cowboySounds
t.fallSounds=["ninjaFall"]
t.style = 'cyborg'


# Powerup Curse ###################################
t = Appearance("CurseMan")
t.colorTexture = "powerupCurse"
t.colorMaskTexture = "bonesColorMask"
t.defaultColor = (0.3,0.5,0.8)
t.defaultHighlight = (1,0,0)
t.iconTexture = t.colorTexture
t.iconMaskTexture = "bonesColorMask"
t.headModel =     "powerup"
t.torsoModel =    "neoSpazTorso"
t.pelvisModel =   "neoSpazPelvis"
t.upperArmModel = "ninjaUpperArm"
t.foreArmModel =  "neoSpazForeArm"
t.handModel =     "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel =     "neoSpazToes"  
t.attackSounds = ['powerup01']
t.jumpSounds = ['powerup01']
t.impactSounds = ["powerdown01"]
t.deathSounds=['powerdown01']
t.pickupSounds = ['tickingCrazy']
t.fallSounds=["powerdown01"]
t.style = 'bones'

#Blessed####################################
t = Appearance("Blessed By God")
t.colorTexture = "powerupHealth"
t.colorMaskTexture = "bonesColorMask"
t.defaultColor = (0.3,0.5,0.8)
t.defaultHighlight = (1,0,0)
t.iconTexture = t.colorTexture
t.iconMaskTexture = "bonesColorMask"
t.headModel =     "powerup"
t.torsoModel =    "neoSpazTorso"
t.pelvisModel =   "neoSpazPelvis"
t.upperArmModel = "ninjaUpperArm"
t.foreArmModel =  "neoSpazForeArm"
t.handModel =     "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel =     "neoSpazToes"  
t.attackSounds = ['powerup01']
t.jumpSounds = ['powerup01']
t.impactSounds = ["powerdown01"]
t.deathSounds=['powerdown01']
t.pickupSounds = ['tickingCrazy']
t.fallSounds=["powerdown01"]
t.style = 'bones'

###############  Hybrid################
t = Appearance("Hybrid")

t.colorTexture = "neoSpazColor"
t.colorMaskTexture = "fontExtras3"
t.defaultColor = (0.3,0.5,0.8)
t.defaultHighlight = (1,0,0)
t.iconTexture = "crossOut"
t.iconMaskTexture = "crossOut"
t.headModel =     "bearHead"
t.torsoModel =    "penguinTorso"
t.pelvisModel =   "pixiePelvis"
t.upperArmModel = "ninjaUpperArm"
t.foreArmModel =  "frostyForeArm"
t.handModel =     "bearHand"
t.upperLegModel = "penguinUpperLeg"
t.lowerLegModel = "penguinLowerLeg"
t.toesModel =     "bearToes"
ninjaSounds =    ['ninja1','ninja2','ninja3','ninja4']
ninjaHitSounds = ['ninjaHit1','ninjaHit2']
t.attackSounds = ninjaSounds
t.jumpSounds = ninjaSounds
t.impactSounds = ninjaHitSounds
t.deathSounds=["ninjaDeath"]
t.pickupSounds = ninjaSounds
t.fallSounds=["ninjaFall"]
t.style = 'bear'




###############  Impact   ##################
t = Appearance("Inact")

t.colorTexture = "zoeColor"
t.colorMaskTexture = "impactBombColorLit"

t.defaultColor = (0.6,0.6,0.6)
t.defaultHighlight = (0,1,0)

t.iconTexture = "powerupImpactBombs"
t.iconMaskTexture = "powerupImpactBombs"

t.headModel = "impactBomb"
t.torsoModel = "cyborgTorso"
t.pelvisModel = "wizardPelvis"
t.upperArmModel = "ninjaUpperArm"
t.foreArmModel = "frostyForeArm"
t.handModel = "agentHead"
t.upperLegModel = "frostyUpperLeg"
t.lowerLegModel = "penguinLowerLeg"
t.toesModel = "agentHead"

t.jumpSounds=["activateBeep"]
t.attackSounds=["LightTurnOn"]
t.impactSounds=["activateBeep"]
t.deathSounds=["impactHard"]
t.fallSounds=["laser"]

t.style = 'cyborg'

###############  Deadman   ##################
t = Appearance("Zombe")

t.colorTexture = "agentColor"
t.colorMaskTexture = "pixieColorMask"

t.defaultColor = (0.6,0.6,0.6)
t.defaultHighlight = (0,1,0)

t.iconTexture = "powerupCurse"
t.iconMaskTexture = "powerupCurse"

t.headModel = "zoeHead"
t.torsoModel = "bonesTorso"
t.pelvisModel = "pixiePelvis"
t.upperArmModel = "frostyUpperArm"
t.foreArmModel = "frostyForeArm"
t.handModel = "bonesHand"
t.upperLegModel = "bonesUpperLeg"
t.lowerLegModel = "pixieLowerLeg"
t.toesModel = "bonesToes"

kronkSounds = ["kronk1",
              "kronk2",
              "kronk3",
              "kronk4",
              "kronk5",
              "kronk6",
              "kronk7",
              "kronk8",
              "kronk9",
              "kronk10"]
t.jumpSounds=kronkSounds
t.attackSounds=kronkSounds
t.impactSounds=kronkSounds
t.deathSounds=["kronkDeath"]
t.pickupSounds=kronkSounds
t.fallSounds=["kronkFall"]


t.style = 'spaz'





###############  CHIDIA  by sparky##################

t = Appearance("Chidia")

t.colorTexture = "powerupHealth"
t.colorMaskTexture = "powerupHealth"

t.defaultColor = (0.5, 0.5, 1)
t.defaultHighlight = (1, 0.5, 0)

t.iconTexture = "powerupHealth"
t.iconMaskTexture = "powerupHealth"

t.headModel =     "penguinHead"
t.torsoModel =    "pixieTorso"
t.pelvisModel = "pixiePelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "pixieForeArm"
t.handModel =     "frostyHand"
t.upperLegModel = "bonesUpperLeg"
t.lowerLegModel = "bonesLowerLeg"
t.toesModel =     "frostyToes"

frostySounds = ['frosty01', 'frosty02', 'frosty03', 'frosty04', 'frosty05']
frostyHitSounds = ['frostyHit01', 'frostyHit02', 'frostyHit03']

t.attackSounds = frostySounds
t.jumpSounds = frostySounds
t.impactSounds = frostyHitSounds
t.deathSounds=["frostyDeath"]
t.pickupSounds = frostySounds
t.fallSounds=["frostyFall"]

t.style = 'frosty'

####################Something by sparky##################
t = Appearance("PrimeLegend")
t.colorTexture = "aliColor"
t.colorMaskTexture = "aliColorMask"
t.defaultColor = (0.3,0.5,0.8)
t.defaultHighlight = (1,0,0)
t.iconTexture =   "aliIcon"
t.iconMaskTexture = "aliIconColorMask"
t.headModel =     "bomb"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "bearPelvis"
t.upperArmModel = "frostyUpperArm"
t.foreArmModel =  "frostyForeArm"
t.handModel =     "agentHand"
t.upperLegModel = "frostyUpperLeg"
t.lowerLegModel = "santaLowerLeg"
t.toesModel =     "flagStand"  
t.attackSounds = ['cyborgFall']
t.jumpSounds = ['bonesFall']
t.impactSounds = ["melHit1"]
t.deathSounds=['pixieDeath']
t.pickupSounds = ['tickingCrazy']
t.fallSounds=["bonesFall"]
t.style = 'bones'

###############  SPAZ   ##################
t = Appearance("Edited Grumbledorf")

t.colorTexture = "wizardColor"
t.colorMaskTexture = "wizardColorMask"

t.iconTexture = "neoSpazIcon"
t.iconMaskTexture = "neoSpazIconColorMask"

t.headModel = "wizardHead"
t.torsoModel = "wizardTorso"
t.pelvisModel = "wizardPelvis"
t.upperArmModel = "wizardUpperArm"
t.foreArmModel = "wizardForeArm"
t.handModel = "wizardHand"
t.upperLegModel = "wizardUpperLeg"
t.lowerLegModel = "wizardLowerLeg"
t.toesModel = "neoSpazToes"

t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["spazFall01"]

t.style = 'pixie'


###############  Zoe   ##################
t = Appearance("Strange Lady")

t.colorTexture = "aliColor"
t.colorMaskTexture = "aliColorMask"

t.defaultColor = (1, 0.5, 0)
t.defaultHighlight = (1, 1, 1)

t.iconTexture = "zoeIcon"
t.iconMaskTexture = "zoeIconColorMask"

t.headModel = "aliHead"
t.torsoModel = "aliTorso"
t.pelvisModel = "frostyPelvis"
t.upperArmModel = "aliUpperArm"
t.foreArmModel = "aliForeArm"
t.handModel = "aliHand"
t.upperLegModel = "aliUpperLeg"
t.lowerLegModel = "aliLowerLeg"
t.toesModel = "aliToes"

t.jumpSounds=["zoeJump01",
              "zoeJump02",
              "zoeJump03"]
t.attackSounds=["zoeAttack01",
                "zoeAttack02",
                "zoeAttack03",
                "zoeAttack04"]
t.impactSounds=["zoeImpact01",
                "zoeImpact02",
                "zoeImpact03",
                "zoeImpact04"]
t.deathSounds=["zoeDeath01"]
t.pickupSounds=["zoePickup01"]
t.fallSounds=["zoeFall01"]

t.style = 'female'


###############  Ninja   ##################
t = Appearance("Samurai")

t.colorTexture = "landMineLit"
t.colorMaskTexture = "ninjaColorMask"

t.defaultColor = (1, 1, 1)
t.defaultHighlight = (0.55, 0.8, 0.55)

t.iconTexture = "ninjaIcon"
t.iconMaskTexture = "ninjaIconColorMask"

t.headModel = "agentHead"
t.torsoModel = "ninjaTorso"
t.pelvisModel = "zoePelvis"
t.upperArmModel = "bonesUpperArm"
t.foreArmModel = "kronkForeArm"
t.handModel = "bearHand"
t.upperLegModel = "aliUpperLeg"
t.lowerLegModel = "aliLowerLeg"
t.toesModel = "ninjaToes"
ninjaAttacks = ['ninjaAttack'+str(i+1)+'' for i in range(7)]
ninjaHits = ['ninjaHit'+str(i+1)+'' for i in range(8)]
ninjaJumps = ['ninjaAttack'+str(i+1)+'' for i in range(7)]

t.jumpSounds=ninjaJumps
t.attackSounds=ninjaAttacks
t.impactSounds=ninjaHits
t.deathSounds=["ninjaDeath1"]
t.pickupSounds=ninjaAttacks
t.fallSounds=["ninjaFall1"]

t.style = 'ninja'


###############  Kronk   ##################
t = Appearance("Werewolf")

t.colorTexture = "kronk"
t.colorMaskTexture = "kronkColorMask"

t.defaultColor = (0.4, 0.5, 0.4)
t.defaultHighlight = (1, 0.5, 0.3)

t.iconTexture = "kronkIcon"
t.iconMaskTexture = "kronkIconColorMask"

t.headModel = "bearHead"
t.torsoModel = "cyborgTorso"
t.pelvisModel = "bunnyPelvis"
t.upperArmModel = "kronkUpperArm"
t.foreArmModel = "kronkForeArm"
t.handModel = "kronkHand"
t.upperLegModel = "bunnyUpperLeg"
t.lowerLegModel = "kronkLowerLeg"
t.toesModel = "kronkToes"

kronkSounds = ["kronk1",
              "kronk2",
              "kronk3",
              "kronk4",
              "kronk5",
              "kronk6",
              "kronk7",
              "kronk8",
              "kronk9",
              "kronk10"]
t.jumpSounds=kronkSounds
t.attackSounds=kronkSounds
t.impactSounds=kronkSounds
t.deathSounds=["kronkDeath"]
t.pickupSounds=kronkSounds
t.fallSounds=["kronkFall"]

t.style = 'kronk'


###############  MEL   ##################
t = Appearance("Strange Alien")

t.colorTexture = "melColor"
t.colorMaskTexture = "melColorMask"

t.defaultColor = (1, 1, 1)
t.defaultHighlight = (0.1, 0.6, 0.1)

t.iconTexture = "melIcon"
t.iconMaskTexture = "melIconColorMask"

t.headModel =     "jackHead"
t.torsoModel =    "penguinTorso"
t.pelvisModel = "frostyPelvis"
t.upperArmModel = "melUpperArm"
t.foreArmModel =  "melForeArm"
t.handModel =     "melHand"
t.upperLegModel = "melUpperLeg"
t.lowerLegModel = "melLowerLeg"
t.toesModel =     "melToes"

melSounds = ["mel01",
              "mel02",
              "mel03",
              "mel04",
              "mel05",
              "mel06",
              "mel07",
              "mel08",
              "mel09",
              "mel10"]

t.attackSounds = melSounds
t.jumpSounds = melSounds
t.impactSounds = melSounds
t.deathSounds=["melDeath01"]
t.pickupSounds = melSounds
t.fallSounds=["melFall01"]

t.style = 'mel'


###############  SANTA   ##################

t = Appearance("Strange Man")

t.colorTexture = "bombColor"
t.colorMaskTexture = "santaColorMask"

t.defaultColor = (1, 0, 0)
t.defaultHighlight = (1, 1, 1)

t.iconTexture = "santaIcon"
t.iconMaskTexture = "santaIconColorMask"

t.headModel =     "kronkHead"
t.torsoModel =    "pixieTorso"
t.pelvisModel = "zoePelvis"
t.upperArmModel = "santaUpperArm"
t.foreArmModel =  "santaForeArm"
t.handModel =     "santaHand"
t.upperLegModel = "wizardUpperLeg"
t.lowerLegModel = "santaLowerLeg"
t.toesModel =     "pixieToes"

hitSounds = ['santaHit01', 'santaHit02', 'santaHit03', 'santaHit04']
sounds = ['santa01', 'santa02', 'santa03', 'santa04', 'santa05']

t.attackSounds = sounds
t.jumpSounds = sounds
t.impactSounds = hitSounds
t.deathSounds=["santaDeath"]
t.pickupSounds = sounds
t.fallSounds=["santaFall"]

t.style = 'santa'

###############  BONES  ##################

t = Appearance("RainbowMb")

t.colorTexture = "rgbStripes"
t.colorMaskTexture = "bonesColorMask"

t.defaultColor = (0.6, 0.9, 1)
t.defaultHighlight = (0.6, 0.9, 1)

t.iconTexture = "bonesIcon"
t.iconMaskTexture = "bonesIconColorMask"

t.headModel =     "impactBomb"
t.torsoModel =    "bonesTorso"
t.pelvisModel =   "bonesPelvis"
t.upperArmModel = "bonesUpperArm"
t.foreArmModel =  "bonesForeArm"
t.handModel =     "bonesHand"
t.upperLegModel = "bonesUpperLeg"
t.lowerLegModel = "bonesLowerLeg"
t.toesModel =     "bonesToes"

bonesSounds =    ['bones1', 'bones2', 'bones3']
bonesHitSounds = ['bones1', 'bones2', 'bones3']

t.attackSounds = bonesSounds
t.jumpSounds = bonesSounds
t.impactSounds = bonesHitSounds
t.deathSounds=["bonesDeath"]
t.pickupSounds = bonesSounds
t.fallSounds=["bonesFall"]

t.style = 'bones'

# bear ###################################

t = Appearance("Mango Colour")

t.colorTexture = "egg4"
t.colorMaskTexture = "bearColorMask"

t.defaultColor = (0.7, 0.5, 0.0)
#t.defaultHighlight = (0.6, 0.5, 0.8)

t.iconTexture = "bearIcon"
t.iconMaskTexture = "bearIconColorMask"

t.headModel =     "bombSticky"
t.torsoModel =    "bonesTorso"
t.pelvisModel =   "bonesPelvis"
t.upperArmModel = "bearUpperArm"
t.foreArmModel =  "bearForeArm"
t.handModel =     "bearHand"
t.upperLegModel = "bearUpperLeg"
t.lowerLegModel = "bearLowerLeg"
t.toesModel =     "bearToes"

bearSounds =    ['bear1', 'bear2', 'bear3', 'bear4']
bearHitSounds = ['bearHit1', 'bearHit2']

t.attackSounds = bearSounds
t.jumpSounds = bearSounds
t.impactSounds = bearHitSounds
t.deathSounds=["bearDeath"]
t.pickupSounds = bearSounds
t.fallSounds=["bearFall"]

t.style = 'bear'

# Penguin ###################################

t = Appearance("Bomb Boy")

t.colorTexture = "penguinColor"
t.colorMaskTexture = "penguinColorMask"

t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)

t.iconTexture = "penguinIcon"
t.iconMaskTexture = "penguinIconColorMask"

t.headModel =     "bomb"
t.torsoModel =    "pixieTorso"
t.pelvisModel =   "kronkPelvis"
t.upperArmModel = "zoeUpperArm"
t.foreArmModel =  "zoeForeArm"
t.handModel =     "melHand"
t.upperLegModel = "melUpperLeg"
t.lowerLegModel = "santaLowerLeg"
t.toesModel =     "santaToes"

penguinSounds =    ['penguin1', 'penguin2', 'penguin3', 'penguin4']
penguinHitSounds = ['penguinHit1', 'penguinHit2']

t.attackSounds = penguinSounds
t.jumpSounds = penguinSounds
t.impactSounds = penguinHitSounds
t.deathSounds=["penguinDeath"]
t.pickupSounds = penguinSounds
t.fallSounds=["penguinFall"]

t.style = 'penguin'

# cyborg ###################################
t = Appearance("Suit-Man")
t.colorTexture = "achievementWall"
t.colorMaskTexture = "ninjaColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "agentHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Army-9000")
t.colorTexture = "towerDLevelColor"
t.colorMaskTexture = "ninjaColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "neoSpazTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Cool Guy")
t.colorTexture = "tipTopPreview"
t.colorMaskTexture = "melColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "neoSpazTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Thug\'s Schoolboy")
t.colorTexture = "tipTopPreview"
t.colorMaskTexture = "ninjaColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "neoSpazTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Gangster")
t.colorTexture = "tipTopPreview"
t.colorMaskTexture = "cyborgColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "neoSpazTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Terminator")
t.colorTexture = "tipTopLevelColor"
t.colorMaskTexture = "cyborgColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Armored Robo-Warrior")
t.colorTexture = "tipTopLevelColor"
t.colorMaskTexture = "melColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Armored Gangster")
t.colorTexture = "tipTopLevelColor"
t.colorMaskTexture = "ninjaColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Nebula")
t.colorTexture = "bar"
t.colorMaskTexture = "ninjaColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Hitman")
t.colorTexture = "achievementOutline"
t.colorMaskTexture = "ninjaColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "agentHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("Humanoid")
t.colorTexture = "bar"
t.colorMaskTexture = "cyborgColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# cyborg ###################################
t = Appearance("HighTech Ape")
t.colorTexture = "menuBG"
t.colorMaskTexture = "melColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "ninjaIconColorMask"
t.headModel =     "ninjaHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'

# Ali ###################################
t = Appearance("PrimeLegend V.2")
t.colorTexture = "cyborgColor"
t.colorMaskTexture = "cyborgColorMask"
t.defaultColor = (1,0.5,0)
t.defaultHighlight = (1,1,1)
t.iconTexture = "agentIcon"
t.iconMaskTexture = "agentIconColorMask"
t.headModel =     "wizardHead"
t.torsoModel =    "kronkTorso"
t.pelvisModel =   "kronkPelvis"
t.upperArmModel = "kronkUpperArm"
t.foreArmModel =  "kronkForeArm"
t.handModel =     "kronkHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "agentToes"
aliSounds =    ['ali1','ali2','ali3','ali4']
aliHitSounds = ['aliHit1','aliHit2']
t.attackSounds = aliSounds
t.jumpSounds = aliSounds
t.impactSounds = aliHitSounds
t.deathSounds=["aliDeath"]
t.pickupSounds = aliSounds
t.fallSounds=["aliFall"]
t.style = 'ali'



# Created by me
t = Appearance("Iceman")

t.colorTexture = "bombColorIce"
t.colorMaskTexture = "bombColorIce"

t.iconTexture = "powerupIceBombs"
t.iconMaskTexture = "powerupIceBombs"

t.headModel = "bomb" 
t.torsoModel = "neoSpazTorso"
t.pelvisModel = "neoSpazPelvis"
t.upperArmModel = "neoSpazUpperArm"
t.foreArmModel = "neoSpazForeArm"
t.handModel = "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel = "neoSpazToes"

t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["spazFall01"]

t.style = 'spaz'


# Created by me
t = Appearance("Cursed")

t.colorTexture = "powerupCurse"
t.colorMaskTexture = "powerupCurse"

t.iconTexture = "powerupCurse"
t.iconMaskTexture = "powerupCurse"

t.headModel = "powerup" 
t.torsoModel = "neoSpazTorso"
t.pelvisModel = "neoSpazPelvis"
t.upperArmModel = "neoSpazUpperArm"
t.foreArmModel = "neoSpazForeArm"
t.handModel = "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel = "neoSpazToes"

t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["spazFall01"]

t.style = 'spaz'


# Created by me ###################################
t = Appearance("Alien-X")
t.colorTexture = "agentColor"
t.colorMaskTexture = "agentColorMask"
t.defaultColor = (0.5,0.5,0.5)
t.defaultHighlight = (1,0,0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "neoSpazHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1','cyborg2','cyborg3','cyborg4']
cyborgHitSounds = ['cyborgHit1','cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'


# Created by me
t = Appearance("Stickyman")

t.colorTexture = "bombStickyColor"
t.colorMaskTexture = "bombStickyColor"

t.iconTexture = "powerupStickyBombs"
t.iconMaskTexture = "powerupStickyBombs"

t.headModel = "bombSticky" 
t.torsoModel = "neoSpazTorso"
t.pelvisModel = "neoSpazPelvis"
t.upperArmModel = "neoSpazUpperArm"
t.foreArmModel = "neoSpazForeArm"
t.handModel = "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel = "neoSpazToes"

t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["spazFall01"]

t.style = 'spaz'


# Created by me
t = Appearance("Impactman")

t.colorTexture = "impactBombColorLit"
t.colorMaskTexture = "impactBombColor"

t.iconTexture = "powerupImpactBombs"
t.iconMaskTexture = "powerupImpactBombs"

t.headModel = "impactBomb" 
t.torsoModel = "cyborgTorso"
t.pelvisModel = "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel = "cyborgForeArm"
t.handModel = "agentHead"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel = "cyborgToes"

t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["spazFall01"]

t.style = 'spaz'


# Created by me
t = Appearance("landMine")

t.colorTexture = "landMine"
t.colorMaskTexture = "landMine"

t.iconTexture = "powerupLandMines"
t.iconMaskTexture = "powerupLandMines"

t.headModel = "landMine" 
t.torsoModel = "neoSpazTorso"
t.pelvisModel = "neoSpazPelvis"
t.upperArmModel = "neoSpazUpperArm"
t.foreArmModel = "neoSpazForeArm"
t.handModel = "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel = "neoSpazToes"

t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["spazFall01"]

t.style = 'spaz'


# Created by Supernova
t = Appearance("Facial")

t.colorTexture = "crossOut"
t.colorMaskTexture = "crossOut"

t.iconTexture = "logo"
t.iconMaskTexture = "logoEaster"

t.headModel = "bomb" 
t.torsoModel = "neoSpazTorso"
t.pelvisModel = "neoSpazPelvis"
t.upperArmModel = "neoSpazUpperArm"
t.foreArmModel = "neoSpazForeArm"
t.handModel = "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel = "neoSpazToes"

t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["spazFall01"]

t.style = 'agent'

# Goku ###################################
t = Appearance("Goku")
t.colorTexture = "gokuColor"
t.colorMaskTexture = "gokuColorMask"
t.defaultColor = (0.3,0.3,0.33)
t.defaultHighlight = (1,0.5,0.3)
t.iconTexture = "gokuIconColor"
t.iconMaskTexture = "gokuIconColorMask"
t.headModel =     "gokuHead"
t.torsoModel =    "gokuTorso"
t.pelvisModel =   "gokuPelvis"
t.upperArmModel = "gokuUpperArm"
t.foreArmModel =  "gokuForeArm"
t.handModel =     "gokuHand"
t.upperLegModel = "gokuUpperLeg"
t.lowerLegModel = "gokuLowerLeg"
t.toesModel =     "gokuToes"
gokuSounds  =    ['goku1','goku2']
gokuHitSounds  = ['gokuHit1','gokuHit2','gokuHit3']
gokuDead       = ['gokuDead']
gokuJump       = ['gokuJump1']
gokuFall       = ['gokuFall']
t.attackSounds = gokuSounds
t.jumpSounds = gokuJump
t.impactSounds = gokuHitSounds
t.deathSounds= gokuDead
t.pickupSounds = gokuSounds
t.fallSounds= gokuFall
t.style = 'agent'

# Vegeta ###################################
t = Appearance("Vegeta")
t.colorTexture = "vegetaColor"
t.colorMaskTexture = "vegetaColorMask"
t.defaultColor = (0.3,0.3,0.33)
t.defaultHighlight = (1,0.5,0.3)
t.iconTexture = "vegetaIconColor"
t.iconMaskTexture = "vegetaIconColorMask"
t.headModel =     "vegetaHead"
t.torsoModel =    "vegetaTorso"
t.pelvisModel =   "vegetaPelvis"
t.upperArmModel = "vegetaUpperArm"
t.foreArmModel =  "vegetaForeArm"
t.handModel =     "vegetaHand"
t.upperLegModel = "vegetaUpperLeg"
t.lowerLegModel = "vegetaLowerLeg"
t.toesModel =     "vegetaToes"
vegetaSounds     = ['vegeta1','vegeta2','vegeta3']
vegetaHitSounds  = ['vegetaHit1','vegetaHit2','vegetaHit3']
vegetaDead       = ['vegetaDead']
vegetaJump       = ['vegetaJump']
vegetaFall       = ['vegetaFall']
t.attackSounds = vegetaSounds
t.jumpSounds = vegetaJump
t.impactSounds = vegetaHitSounds
t.deathSounds= vegetaDead
t.pickupSounds = vegetaSounds
t.fallSounds= vegetaFall
t.style = 'agent'

# Android ###################################
t = Appearance("Android")
t.colorTexture = "androidColor"
t.colorMaskTexture = "androidColorMask"
t.defaultColor = (1,1,1)
t.defaultHighlight = (0,0,0)
t.iconTexture = "androidIcon"
t.iconMaskTexture = "androidIconColorMask"
t.headModel =     "androidHead"
t.torsoModel =    "androidTorso"
t.pelvisModel =   "zero"
t.upperArmModel = "androidArm"
t.foreArmModel =  "zero"
t.handModel =     "zero"
t.upperLegModel = "androidLeg"
t.lowerLegModel = "zero"
t.toesModel =     "zero"
alienSounds =    ['alien1','alien2','alien3','alien4']
alienHitSounds = ['alienHit1','alienHit2']
t.attackSounds = alienSounds
t.jumpSounds = alienSounds
t.impactSounds = alienHitSounds
t.deathSounds=["alienDeath"]
t.pickupSounds = alienSounds
t.fallSounds=["alienFall"]
t.style = 'agent'

# AVGN ###################################
t = Appearance("AVGN")
t.colorTexture = "avgnColor"
t.colorMaskTexture = "avgnColorMask"
t.defaultColor = (1,1,1)
t.defaultHighlight = (0.53,0.28,0.14)
t.iconTexture = "avgnIcon"
t.iconMaskTexture = "avgnIconColorMask"
t.headModel =     "agentHead"
t.torsoModel =    "agentTorso"
t.pelvisModel =   "agentPelvis"
t.upperArmModel = "agentUpperArm"
t.foreArmModel =  "agentForeArm"
t.handModel =     "agentHand"
t.upperLegModel = "agentUpperLeg"
t.lowerLegModel = "agentLowerLeg"
t.toesModel =     "agentToes"
agentSounds =    ['avgn1','avgn2','avgn3','avgn4']
agentHitSounds = ['avgnPain1','avgnPain2','avgnPain3']
t.attackSounds = agentSounds
t.jumpSounds = agentSounds
t.impactSounds = agentHitSounds
t.deathSounds=["avgnDeath1","avgnDeath2","avgnDeath3","avgnDeath4","avgnDeath5"]
t.pickupSounds = agentSounds
t.fallSounds=["avgnFall1","avgnFall2","avgnFall3"]
t.style = 'agent'

# Powerup Curse ###################################
t = Appearance("Cursed")
t.colorTexture = "powerupCurse"
t.colorMaskTexture = "bonesColorMask"
t.defaultColor = (0.3,0.5,0.8)
t.defaultHighlight = (1,0,0)
t.iconTexture = t.colorTexture
t.iconMaskTexture = "bonesColorMask"
t.headModel =     "powerup"
t.torsoModel =    "neoSpazTorso"
t.pelvisModel =   "neoSpazPelvis"
t.upperArmModel = "zero"
t.foreArmModel =  "neoSpazForeArm"
t.handModel =     "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel =     "neoSpazToes"  
t.attackSounds = ['powerup01']
t.jumpSounds = ['powerup01']
t.impactSounds = ["powerdown01"]
t.deathSounds=['powerdown01']
t.pickupSounds = ['ticking']
t.fallSounds=["powerdown01"]
t.style = 'spaz'

###############  FROSHLEE14   ################## IT'S ME!!
t = Appearance("Froshlee")
t.colorTexture = "froshlee"
t.colorMaskTexture = "froshColorMask"
t.iconTexture = "froshIcon"
t.iconMaskTexture = "froshIconColorMask"
t.headModel = "froshHead"
t.torsoModel = "froshTorso"
t.pelvisModel = "zero"
t.upperArmModel = "froshUpperArm"
t.foreArmModel = "froshForeArm"
t.handModel = "zero"
t.upperLegModel = "froshUpperLeg"
t.lowerLegModel = "froshLowerLeg"
t.toesModel = "zero"
t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["froshDeath"]
t.style = 'agent'

# JuiceBoy ###################################
t = Appearance("Juice-Boy")
t.colorTexture = "juiceBoyColor"
t.colorMaskTexture = "juiceBoyColorMask"
t.defaultColor = (0.2,1,0.2)
t.defaultHighlight = (1,1,0)
t.iconTexture = "juiceBoyIcon"
t.iconMaskTexture = "juiceBoyIconColorMask"
t.headModel =     "zero"
t.torsoModel =    "juiceBoyTorso"
t.pelvisModel =   "zero"
t.upperArmModel = "juiceBoyUpperArm"
t.foreArmModel =  "juiceBoyForeArm"
t.handModel =     "juiceBoyHand"
t.upperLegModel = "juiceBoyUpperLeg"
t.lowerLegModel = "juiceBoyLowerLeg"
t.toesModel =     "juiceBoyToes"
juiceSounds = ['juice1','juice2','juice3','juice4','juice5','juice6']
t.attackSounds = juiceSounds
t.jumpSounds = juiceSounds
t.impactSounds = juiceSounds
t.deathSounds = ["juiceDeath"]
t.pickupSounds = juiceSounds
t.fallSounds = ["juiceFall"]
t.style = 'agent'

# Mictlan ###################################
t = Appearance("Mictlan")
t.colorTexture = "mictlanColor"
t.colorMaskTexture = "mictlanColorMask"
t.defaultColor = (0.1,1,1)
t.defaultHighlight = (0.1,0.1,0.1)
t.iconTexture = "mictlanIcon"
t.iconMaskTexture = "mictlanIconColorMask"
t.headModel =     "zero"
t.torsoModel =    "mictlanTorso"
t.pelvisModel =   "aliPelvis"
t.upperArmModel = "mictlanUpperArm"
t.foreArmModel =  "mictlanForeArm"
t.handModel =     "mictlanHand"
t.upperLegModel = "mictlanUpperLeg"
t.lowerLegModel = "mictlanLowerLeg"
t.toesModel =     "mictlanToes"
mictlanSounds =    ['mictlan1','mictlan2','mictlan3','mictlan4','mictlan5','mictlan6','mictlan7','mictlan8']
mictlanHitSounds = ['mictlanPain1','mictlanPain2','mictlanPain3']
t.attackSounds = mictlanSounds
t.jumpSounds = mictlanSounds
t.impactSounds = mictlanHitSounds
t.deathSounds=["mictlanDeath"]
t.pickupSounds = mictlanSounds
t.fallSounds=["mictlanFall"]
t.style = 'agent'

# Milk (Cow Character) ###################################
t = Appearance("Milk")
t.colorTexture = "cowColor"
t.colorMaskTexture = "cowColorMask"
t.defaultColor = (1,1,1)
t.defaultHighlight = (1,0.3,0.5)
t.iconTexture = "cowIcon"
t.iconMaskTexture = "cowIconColorMask"
t.headModel =     "cowHead"
t.torsoModel =    "cowTorso"
t.pelvisModel =   "cowPelvis"
t.upperArmModel = "cowUpperArm"
t.foreArmModel =  "cowForeArm"
t.handModel =     "cowHand"
t.upperLegModel = "cowUpperLeg"
t.lowerLegModel = "cowLowerLeg"
t.toesModel =     "cowToes"
cowSounds =    ['cow1','cow2','cow3','cow4']
t.attackSounds = cowSounds
t.jumpSounds = cowSounds
t.impactSounds = cowSounds
t.deathSounds = ["cowDeath"]
t.pickupSounds = cowSounds
t.fallSounds = ["cowFall"]
t.style = 'bear'

# Goku ###################################
t = Appearance("Goku")
t.colorTexture = "gokuColor"
t.colorMaskTexture = "gokuColorMask"
t.defaultColor = (0.3,0.3,0.33)
t.defaultHighlight = (1,0.5,0.3)
t.iconTexture = "gokuIconColor"
t.iconMaskTexture = "gokuIconColorMask"
t.headModel =     "gokuHead"
t.torsoModel =    "gokuTorso"
t.pelvisModel =   "gokuPelvis"
t.upperArmModel = "gokuUpperArm"
t.foreArmModel =  "gokuForeArm"
t.handModel =     "gokuHand"
t.upperLegModel = "gokuUpperLeg"
t.lowerLegModel = "gokuLowerLeg"
t.toesModel =     "gokuToes"
gokuSounds  =    ['goku1','goku2']
gokuHitSounds  = ['gokuHit1','gokuHit2','gokuHit3']
gokuDead       = ['gokuDead']
gokuJump       = ['gokuJump1']
gokuFall       = ['gokuFall']
t.attackSounds = gokuSounds
t.jumpSounds = gokuJump
t.impactSounds = gokuHitSounds
t.deathSounds= gokuDead
t.pickupSounds = gokuSounds
t.fallSounds= gokuFall
t.style = 'agent'

###############  DJ   ##################
t = Appearance("Marshmallow")
t.colorTexture = "marshmalloColor2"
t.colorMaskTexture = "marshmalloColorMask"
t.iconTexture = "marshmalloIcon"
t.iconMaskTexture = "marshmalloIconMask"
t.headModel = "marshmalloHead"
t.torsoModel = "marshmalloTorso"
t.pelvisModel = "marshmalloPelvis"
t.upperArmModel = "marshmalloUpperArm"
t.foreArmModel = "marshmalloForeArm"
t.handModel = "marshmalloHand"
t.upperLegModel = "marshmalloUpperLeg"
t.lowerLegModel = "marshmalloLowerLeg"
t.toesModel = "marshmalloToes"
t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["froshDeath"]
t.style = 'agent'

# Saitama ##################################
#Saitama by ANG3L#
t = Appearance("Saitama")

t.colorTexture = "saitamaColor"
t.colorMaskTexture = "saitamaColorMask"

t.defaultColor = (0.7,0.5,0.0)

t.iconTexture = "saitamaIcon"
t.iconMaskTexture = "saitamaIconMask"

t.headModel =     "saitamaHead"
t.torsoModel =    "saitamaTorso"
t.pelvisModel =   "saitamaPelvis"
t.upperArmModel = "saitamaUpperArm"
t.foreArmModel =  "saitamaForeArm"
t.handModel =     "saitamaHand"
t.upperLegModel = "saitamaUpperLeg"
t.lowerLegModel = "saitamaLowerLeg"
t.toesModel =     "saitamaToes"

saitamaSounds =    ['saitama1','saitama2','saitama3','saitama4']
saitamaHitSounds = ['saitamaHit1','saitamaHit2']
saitamaJumpSounds = ['saitamaJump']

t.attackSounds = saitamaSounds
t.jumpSounds = saitamaJumpSounds
t.impactSounds = saitamaHitSounds
t.deathSounds=["saitamaDeath"]
t.pickupSounds = saitamaSounds
t.fallSounds=["saitamaFall"]

t.style = 'agent'

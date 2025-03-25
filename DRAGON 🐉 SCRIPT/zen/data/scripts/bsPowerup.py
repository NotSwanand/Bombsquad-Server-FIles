# -*- coding: utf-8 -*-
import sys
import random
import weakref
import bs
import bsUI
import bsUtils
import BuddyBunny
import settings


defaultPowerupInterval = 8000


class PowerupMessage(object):
    """
    category: Message Classes

    Tell something to get a powerup.
    This message is normally recieved by touching
    a bs.Powerup box.

    Attributes:

       powerupType
          The type of powerup to be granted (a string).
          See bs.Powerup.powerupType for available type values.

       sourceNode
          The node the powerup game from, or an empty bs.Node ref otherwise.
          If a powerup is accepted, a bs.PowerupAcceptMessage should be sent
          back to the sourceNode to inform it of the fact. This will generally
          cause the powerup box to make a sound and disappear or whatnot.
    """
    def __init__(self, powerupType, sourceNode=bs.Node(None)):
        """
        Instantiate with given values.
        See bs.Powerup.powerupType for available type values.
        """
        self.powerupType = powerupType
        self.sourceNode = sourceNode


class PowerupAcceptMessage(object):
    """
    category: Message Classes

    Inform a bs.Powerup that it was accepted.
    This is generally sent in response to a bs.PowerupMessage
    to inform the box (or whoever granted it) that it can go away.
    """
    pass


class _TouchedMessage(object):
    pass


class PowerupFactory(object):
    """
    category: Game Flow Classes

    Wraps up media and other resources used by bs.Powerups.
    A single instance of this is shared between all powerups
    and can be retrieved via bs.Powerup.getFactory().

    Attributes:

       model
          The bs.Model of the powerup box.

       modelSimple
          A simpler bs.Model of the powerup box, for use in shadows, etc.

       texBox
          Triple-bomb powerup bs.Texture.

       texPunch
          Punch powerup bs.Texture.

       texIceBombs
          Ice bomb powerup bs.Texture.

       texStickyBombs
          Sticky bomb powerup bs.Texture.

       texShield
          Shield powerup bs.Texture.

       texImpactBombs
          Impact-bomb powerup bs.Texture.

       texHealth
          Health powerup bs.Texture.

       texLandMines
          Land-mine powerup bs.Texture.

       texCurse
          Curse powerup bs.Texture.

       healthPowerupSound
          bs.Sound played when a health powerup is accepted.

       powerupSound
          bs.Sound played when a powerup is accepted.

       powerdownSound
          bs.Sound that can be used when powerups wear off.

       powerupMaterial
          bs.Material applied to powerup boxes.

       powerupAcceptMaterial
          Powerups will send a bs.PowerupMessage to anything they touch
          that has this bs.Material applied.
    """

    def __init__(self):
        """
        Instantiate a PowerupFactory.
        You shouldn't need to do this; call bs.Powerup.getFactory()
        to get a shared instance.
        """
        self._lastPowerupType = None

        self.model = bs.getModel('powerup')
        self.modelSimple = bs.getModel('powerupSimple')
        self.snoModel = bs.getModel('frostyPelvis')

        self.texBomb = bs.getTexture('powerupBomb')
        self.texPunch = bs.getTexture('powerupPunch')
        self.texIceBombs = bs.getTexture('powerupIceBombs')
        self.texStickyBombs = bs.getTexture('powerupStickyBombs')
        self.texShield = bs.getTexture('powerupShield')
        self.texImpactBombs = bs.getTexture('powerupImpactBombs')
        self.texHealth = bs.getTexture('powerupHealth')
        self.texLandMines = bs.getTexture('powerupLandMines')
        self.texCurse = bs.getTexture('powerupCurse')
        self.texStickyForce = bs.getTexture('sparks')
        self.texSpeed = bs.getTexture('powerupSpeed')
        self.texCannon = bs.getTexture('googlePlayLeaderboardsIcon')
        self.texArtillery = bs.getTexture('upButton')
        self.texElonMuskMine = bs.getTexture('ouyaAButton')
        self.texAirstrike = bs.getTexture('achievementDualWielding')
        self.texHighJump = bs.getTexture('buttonJump')
        self.texSno = bs.getTexture('bunnyColor')
        self.texRailgun = bs.getTexture('ouyaYButton')

        self.healthPowerupSound = bs.getSound('healthPowerup')
        self.powerupSound = bs.getSound('powerup01')
        self.powerdownSound = bs.getSound('powerdown01')
        self.dropSound = bs.getSound('boxDrop')

        # material for powerups
        self.powerupMaterial = bs.Material()

        # material for anyone wanting to accept powerups
        self.powerupAcceptMaterial = bs.Material()

        # pass a powerup-touched message to applicable stuff
        self.powerupMaterial.addActions(
            conditions=(('theyHaveMaterial', self.powerupAcceptMaterial)),
            actions=(('modifyPartCollision', 'collide', True),
                     ('modifyPartCollision', 'physical', False),
                     ('message', 'ourNode', 'atConnect', _TouchedMessage())))

        # we dont wanna be picked up
        self.powerupMaterial.addActions(
            conditions=('theyHaveMaterial',
                        bs.getSharedObject('pickupMaterial')),
            actions=(('modifyPartCollision', 'collide', False)))

        self.powerupMaterial.addActions(
            conditions=('theyHaveMaterial',
                        bs.getSharedObject('footingMaterial')),
            actions=(('impactSound', self.dropSound, 0.5, 0.1)))

        self._powerupDist = []
        for p, freq in getDefaultPowerupDistribution():
            for i in range(int(freq)):
                self._powerupDist.append(p)

    def getRandomPowerupType(self, forceType=None, excludeTypes=[]):
        """
        Returns a random powerup type (string).
        See bs.Powerup.powerupType for available type values.

        There are certain non-random aspects to this; a 'curse' powerup,
        for instance, is always followed by a 'health' powerup (to keep things
        interesting). Passing 'forceType' forces a given returned type while
        still properly interacting with the non-random aspects of the system
        (ie: forcing a 'curse' powerup will result
        in the next powerup being health).
        """
        if forceType:
            t = forceType
        else:
            # if the last one was a curse, make this one a health to
            # provide some hope
            if self._lastPowerupType == 'curse':
                t = 'health'
            else:
                while True:
                    t = self._powerupDist[
                        random.randint(0, len(self._powerupDist)-1)]

                    if t not in excludeTypes:
                        break

        self._lastPowerupType = t
        return t


def getDefaultPowerupDistribution():
    return (
            ('tripleBombs', 5),
            ('iceBombs', 3),
            ('punch', 0),
            ('impactBombs', 3),
            ('stickyBombs', 5),
            ('landMines', 3),
            ('shield', 0),
            ('stickyForce', 1),
            ('speed', 1),
            ('elonMine', 1),
            ('airstrike', 1),
            ('artillery', 1),
            ('highJump', 2),
            ('railgun', 0),
            ('cannon', 1),
            ('health', 1),
            ('curse', 1)
            )


class Powerup(bs.Actor):
    """
    category: Game Flow Classes

    A powerup box.
    This will deliver a bs.PowerupMessage to anything that touches it
    which has the bs.PowerupFactory.powerupAcceptMaterial applied.

    Attributes:

       powerupType
          The string powerup type.  This can be 'tripleBombs', 'punch',
          'iceBombs', 'impactBombs', 'landMines', 'stickyBombs', 'shield',
          'health', or 'curse'.

       node
          The 'prop' bs.Node representing this box.
    """
    def __init__(self, position=(0, 1, 0), powerupType='tripleBombs',
                 expire=True):
        """
        Create a powerup-box of the requested type at the requested position.

        see bs.Powerup.powerupType for valid type strings.
        """

        bs.Actor.__init__(self)
        factory = self.getFactory()
        self.powerupType = powerupType
        self._powersGiven = False

        mod = factory.model
        mScl = 1
        color = (1, 1, 1)
        name = "none"

        if powerupType == 'tripleBombs':
            tex = factory.texBomb
            name = "| TRIPLE BOMBS |"            

        elif powerupType == 'punch':
            tex = factory.texPunch
            name = "| GLOVES |"

        elif powerupType == 'railgun':
            tex = factory.texRailgun
            name = "| KAMEHAMEHA |"

        elif powerupType == 'iceBombs':
            tex = factory.texIceBombs
            name = "| ICE BOMBS |"

        elif powerupType == 'impactBombs':
            tex = factory.texImpactBombs
            name = "| IMPACT BOMBS |"

        elif powerupType == 'landMines':
            tex = factory.texLandMines
            name = "| LAND MINES |"

        elif powerupType == 'stickyBombs':
            tex = factory.texStickyBombs
            name = "| STICKY BOMBS |"

        elif powerupType == 'shield':
            tex = factory.texShield
            name = "| SHIELD |"

        elif powerupType == 'health':
            tex = factory.texHealth
            name = "| HEALTH |"

        elif powerupType == 'curse':
            tex = factory.texCurse
            name = "| CURSE |"

        elif powerupType == 'speed':
            tex = factory.texSpeed
            name = "| SPEED |"

        elif powerupType == 'stickyForce':
            tex = factory.texStickyForce
            name = "| ANTI GRAVITY |"

        elif powerupType == 'cannon':
            tex = factory.texCannon
            name = "| BAZUKA |"

        elif powerupType == 'artillery':
            tex = factory.texArtillery
            name = "| RAINING DEATH |"

        elif powerupType == 'elonMine':
            tex = factory.texElonMuskMine
            name = "| XTREME SKULL! |"

        elif powerupType == 'airstrike':
            tex = factory.texAirstrike
            name = "| AIR STRIKE |"

        elif powerupType == 'highJump':
            tex = factory.texHighJump
            name = "| HIGH JUMP |"

        else:
            raise Exception('invalid powerupType: '+str(powerupType))

        if len(position) != 3:
            raise Exception('expected 3 floats for position')

        self.node = bs.newNode(
            'prop',
            delegate=self,
            attrs={'body':'box',
                   'position':position,
                   'model':factory.model,
                   'lightModel':factory.modelSimple,
                   'shadowSize':0.5,
                   'colorTexture':tex,
                   'reflection':'powerup',
                   'reflectionScale':[1.0],
                   'materials':(factory.powerupMaterial,
                                bs.getSharedObject('objectMaterial'))})
        prefixAnim = {0: (1, 0, 0), 250: (1, 1, 0), 250 * 2: (0, 1, 0), 250 * 3: (0, 1, 1), 250 * 4: (1, 0, 1),
                      250 * 5: (0, 0, 1), 250 * 6: (1, 0, 0)}
        color = (random.random(), random.random(), random.random())
        if settings.nameOnPowerUps:
            m = bs.newNode('math', owner=self.node, attrs={'input1': (0, 0.7, 0), 'operation': 'add'})
            self.node.connectAttr('position', m, 'input2')
            self.nodeText = bs.newNode('text',
                                       owner=self.node,
                                       attrs={'text': str(name),
                                              'inWorld': True,
                                              'shadow': 1.0,
                                              'flatness': 1.0,
                                              'color': color,
                                              'scale': 0.0,
                                              'hAlign': 'center'})
            m.connectAttr('output', self.nodeText, 'position')
            bs.animate(self.nodeText, 'scale', {0: 0, 140: 0.016, 200: 0.01})
            bsUtils.animateArray(self.nodeText, 'color', 3, prefixAnim, True)
            bs.emitBGDynamics(position=self.nodeText.position, velocity=self.node.position, count=10, scale=0.4,
                              spread=0.01, chunkType='sweat')
        if settings.discoLightsOnPowerUps:
            self.nodeLight = bs.newNode('light',
                                        attrs={'position': self.node.position,
                                               'color': color,
                                               'radius': 0.05,
                                               'volumeIntensityScale': 0.03})
            self.node.connectAttr('position', self.nodeLight, 'position')
            bsUtils.animateArray(self.nodeLight, 'color', 3, prefixAnim, True)

        if settings.shieldOnPowerUps:
            self.nodeShield = bs.newNode('shield', owner=self.node, attrs={'color': color,
                                                                           'position': (
                                                                               self.node.position[0],
                                                                               self.node.position[1],
                                                                               self.node.position[2] + 0.5),
                                                                           'radius': 0.8})
            self.node.connectAttr('position', self.nodeShield, 'position')
            bsUtils.animateArray(self.nodeShield, 'color', 3, prefixAnim, True)

        # animate in..
        curve = bs.animate(self.node,"modelScale",{0:0,140:1.6,200:1})
        bs.gameTimer(200,curve.delete)

        if expire:
            bs.gameTimer(defaultPowerupInterval-2500,
                         bs.WeakCall(self._startFlashing))
            bs.gameTimer(defaultPowerupInterval-1000,
                         bs.WeakCall(self.handleMessage, bs.DieMessage()))

    @classmethod
    def getFactory(cls):
        """
        Returns a shared bs.PowerupFactory object, creating it if necessary.
        """
        activity = bs.getActivity()
        if activity is None:
            raise Exception('no current activity')

        try:
            return activity._sharedPowerupFactory
        except Exception:
            f = activity._sharedPowerupFactory = PowerupFactory()
            return f

    def _startFlashing(self):
        if self.node.exists():
            self.node.flashing = True

    def handleMessage(self, m):
        self._handleMessageSanityCheck()
        if isinstance(m, PowerupAcceptMessage):
            factory = self.getFactory()
            if self.powerupType == 'health':
                bs.playSound(factory.healthPowerupSound, 3,
                             position=self.node.position)

            bs.playSound(factory.powerupSound, 3,
                         position=self.node.position)
            self._powersGiven = True
            self.handleMessage(bs.DieMessage())

        elif isinstance(m, _TouchedMessage):
            if not self._powersGiven:
                node = bs.getCollisionInfo("opposingNode")
                if node is not None and node.exists():
                    node.handleMessage(PowerupMessage(self.powerupType,
                                                      sourceNode=self.node))

        elif isinstance(m, bs.DieMessage):
            if self.node.exists():
                if (m.immediate):
                    self.node.delete()
                else:
                    curve = bs.animate(self.node, "modelScale", {0:1,100:0})
                    bs.gameTimer(100, self.node.delete)

        elif isinstance(m, bs.OutOfBoundsMessage):
            self.handleMessage(bs.DieMessage())

        elif isinstance(m, bs.HitMessage):
            # dont die on punches (thats annoying)
            if m.hitType != 'punch':
                self.handleMessage(bs.DieMessage())
        else:
            bs.Actor.handleMessage(self, m)

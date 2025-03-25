import bs
from bsMap import *
import bsMap
from random import randrange
from settings import *
count = len(texts)


def __init__(self, vrOverlayCenterOffset=None):
        """
        Instantiate a map.
        """
        import bsInternal
        bs.Actor.__init__(self)
        self.preloadData = self.preload(onDemand=True)

        def text():
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue043THIS SERVER IS OWNED BY \ue048ZEN-OH SAMA\ue048  and IRON MAN\ue043',
                              'scale':1.1,
                              'maxWidth':0,
                              'position':(0,170),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0: 0.0,500: 1.0,4500: 1.0,5000: 0.0})
                bs.gameTimer(5000,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue048THIS SERVER USES SCRIPT EDITED BY ZEN-OH SAMA\ue048',
                              'scale':1.1,
                              'maxWidth':0,
                              'position':(0,170),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{9000: 0.0,9500: 1.0,13500: 1.0,14000: 0.0})
                bs.gameTimer(14000,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue043THE BEST PLAYER ON THE SERVER IS \n\ue048ZEN-OH SAMA\ue048\n\ue048LOL THAT`S ME :D\ue048',
                              'scale':1.1,
                              'maxWidth':0,
                              'position':(0,170),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{17500: 0.0,18000: 1.0,22000: 1.0,22500: 0.0})
                bs.gameTimer(22500,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue048WHAT YOU SHOULD DO:\ue048\n\ue044 1. DONT ASK FOR ADMINSHIP!\ue044\n \ue044 2. DONT ABUSE AND RESPECT OTHERS\ue044\n\ue044 3. SUBSCRIBE TO PEWDIEPIE AND DARKLORD GAMING!\ue044',
                              'scale':1.1,
                              'maxWidth':0,
                              'position':(0,170),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{26500: 0.0,27000: 1.0,31000: 1.0,31500: 0.0})
                bs.gameTimer(31500,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue048NEED ANY HELP! CONTACT ZEN-OH SAMA ON DISCORD\ue048\n \ue044 DISCORD ID -ZEN-OH SAMA#5559\ue044\n \ue048 THANKS FOR LOVING MY SERVER :D\ue048',
                              'scale':1.1,
                              'maxWidth':0,
                              'position':(0,170),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{35500: 0.0,36000: 1.0,40000: 1.0,40500: 0.0})
                bs.gameTimer(40500,t.delete)
        bs.gameTimer(3500,bs.Call(text))
        bs.gameTimer(49500,bs.Call(text),repeat = True)

	def recurringText():
                t = bs.newNode('text',
                       attrs={ 'text':texts[randrange(count)],
                              'scale':0.95,
                              'maxWidth':0,
                              'position':(0,120),
                              'shadow':0.5,
                              'flatness':1.0,
                              'color':((0.2+random.random()*0.8),(0.2+random.random()*0.8),(0.2+random.random()*0.8)),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0: 0.0,500: 0.8,5500: 0.8,6000: 0.0})
                bs.gameTimer(6000,t.delete)
        bs.gameTimer(10,bs.Call(text))
	import settings
	if settings.enableCoinSystem:
		bs.gameTimer(10,bs.Call(recurringText))
		bs.gameTimer(6000,bs.Call(recurringText),repeat = True)
        
        # set some defaults
        bsGlobals = bs.getSharedObject('globals')
        # area-of-interest bounds
        aoiBounds = self.getDefBoundBox("areaOfInterestBounds")
        if aoiBounds is None:
            print 'WARNING: no "aoiBounds" found for map:',self.getName()
            aoiBounds = (-1,-1,-1,1,1,1)
        bsGlobals.areaOfInterestBounds = aoiBounds
        # map bounds
        mapBounds = self.getDefBoundBox("levelBounds")
        if mapBounds is None:
            print 'WARNING: no "levelBounds" found for map:',self.getName()
            mapBounds = (-30,-10,-30,30,100,30)
        bsInternal._setMapBounds(mapBounds)
        # shadow ranges
        try: bsGlobals.shadowRange = [
                self.defs.points[v][1] for v in 
                ['shadowLowerBottom','shadowLowerTop',
                 'shadowUpperBottom','shadowUpperTop']]
        except Exception: pass
        # in vr, set a fixed point in space for the overlay to show up at..
        # by default we use the bounds center but allow the map to override it
        center = ((aoiBounds[0]+aoiBounds[3])*0.5,
                  (aoiBounds[1]+aoiBounds[4])*0.5,
                  (aoiBounds[2]+aoiBounds[5])*0.5)
        if vrOverlayCenterOffset is not None:
            center = (center[0]+vrOverlayCenterOffset[0],
                      center[1]+vrOverlayCenterOffset[1],
                      center[2]+vrOverlayCenterOffset[2])
        bsGlobals.vrOverlayCenter = center
        bsGlobals.vrOverlayCenterEnabled = True
        self.spawnPoints = self.getDefPoints("spawn") or [(0,0,0,0,0,0)]
        self.ffaSpawnPoints = self.getDefPoints("ffaSpawn") or [(0,0,0,0,0,0)]
        self.spawnByFlagPoints = (self.getDefPoints("spawnByFlag")
                                  or [(0,0,0,0,0,0)])
        self.flagPoints = self.getDefPoints("flag") or [(0,0,0)]
        self.flagPoints = [p[:3] for p in self.flagPoints] # just want points
        self.flagPointDefault = self.getDefPoint("flagDefault") or (0,1,0)
        self.powerupSpawnPoints = self.getDefPoints("powerupSpawn") or [(0,0,0)]
        self.powerupSpawnPoints = \
            [p[:3] for p in self.powerupSpawnPoints] # just want points
        self.tntPoints = self.getDefPoints("tnt") or []
        self.tntPoints = [p[:3] for p in self.tntPoints] # just want points
        self.isHockey = False
        self.isFlying = False
        self._nextFFAStartIndex = 0
        
bsMap.Map.__init__ = __init__

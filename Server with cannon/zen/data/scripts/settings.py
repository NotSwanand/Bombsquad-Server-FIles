import bs
enableTop5effects = True
enableTop5commands = False
enableCoinSystem = True

texts = ['WELCOME TO ZEN-OH SAMA"S SERVER!','Use "/shop commands" to see commands available to buy.','Use "/shop effects" to see effects available and their price.','Use "/me" or "/stats" to see your '+bs.getSpecialChar('ticket')+' and your stats in this server', 'Use "/buy" to buy effects that you like','Use "/donate" to give some of your tickets to other players','Use "/scoretocash" to convert some of your score to '+bs.getSpecialChar('ticket')+'\nCurrent Rate: 5scores = '+bs.getSpecialChar('ticket')+'1']

questionDelay = 60 #seconds
questionsList = {'Who is the owner of this server?': 'zen oh sama', 
       'add': None, 
       'multiply': None}

availableCommands = {'/nv': 50, 
   '/ooh': 5, 
   '/playSound': 10, 
   '/box': 30, 
   '/boxall': 60, 
   '/spaz': 50, 
   '/spazall': 100, 
   '/inv': 40, 
   '/invall': 80, 
   '/tex': 20, 
   '/texall': 40, 
   '/freeze': 60, 
   '/freezeall': 100, 
   '/sleep': 40, 
   '/sleepall': 80, 
   '/thaw': 50, 
   '/thawall': 70, 
   '/kill': 80, 
   '/killall': 150, 
   '/end': 100, 
   '/hug': 60, 
   '/hugall': 100, 
   '/tint': 90, 
   '/sm': 50, 
   '/fly': 50, 
   '/flyall': 100, 
   '/heal': 50, 
   '/healall': 70, 
   '/gm': 200, 
   '/custom': 250}

availableEffects = {'ice': 500, 
   'sweat': 750, 
   'scorch': 500, 
   'glow': 400, 
   'distortion': 750, 
   'slime': 500, 
   'metal': 500, 
   'surrounder': 1000}

joinNotification = True  # Whether or not to show the notification when a player joins

leaveNotification = True  # Whether or not to show the notification when a player leaves

nameOnPowerUps = True  # Whether or not to show the powerup's name on top of powerups

shieldOnPowerUps = True  # Whether or not to add shield on powerups

discoLightsOnPowerUps = True  # Whether or not to show disco lights on powerup's location

FlyMaps = True  # Whether or not to enable the 3D flying maps in games playlist

generateStats = True  # Whether or not to generate the html stats of the server

botFile = True  # Whether or not to generate the file to be read by my discord bot,
# botFile won't work if `generateStats` is False

partyName = "SPIDERMAN IS BACK"  # Type your party's name here.

filteredWords = ["fuck", "motherfucker", "sex", "chutiya", "gandu", "bhosdike", "chutiye", "f**k", "teri maa ki chut", "chut", "Lund", "porn", "Fuck", "Motherfucker", "Sex", "Chutiya", "Gandu", "Bhosdike", "Chutiye", "F**K", "Teri maa ki chut", "Chut", "Lund", "Porn"]  # Some words to filter from the chat messages in the party.

showFilteredMessage = True  # Whether to show the message containing restricted word after removing the word or not.

replaceText = "**RESTRICTED WORD FILTERED BY SERVER**\nDon\'t Abuse or You Will be Kicked"  # The string to replace the filtered words with.

kickAbusers = True  # Whether to kick or not the players who use filtered words.

abuserBanTiming = 1000000  # The time upto which the kicked abusers may not join the server after being kicked.

showScoresInTopRightCorner = True


def return_yielded_game_texts():
    for text in gameTexts:
        yield text


def return_players_yielded(bs):
    for player in bs.getSession().players:
        yield player

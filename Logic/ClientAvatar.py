import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))

class LogicClientAvatar(Writer):

    def encode(self):

        self.writeInt(0)

        self.writeInt(config['AccountHighID'])  # DefaultHighID
        self.writeInt(config['AccountLowID'])  # DefaultLowID
        self.writeInt(config['HomeHighID'])  # CurrentHomeHighID
        self.writeInt(config['HomeLowID'])  # CurrentHomeLowID

        self.writeByte(1)  # IsInAlliance

        self.writeInt(config['AllianceHighID'])  # AllianceHighID
        self.writeInt(config['AllianceLowID'])  # AllianceLowID

        self.writeString(config['AllianceName'])  # AllianceName

        self.writeInt(config['AllianceBadge'])  # AllianceBadge
        self.writeInt(config['AllianceRole'])  # AllianceRole

        self.writeByte(0)

        self.writeInt(0)
        self.writeInt(1)

        self.writeInt(0)
        self.writeInt(10)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString(config['Name'])  # Name
        self.writeString(None)  # FacebookID

        self.writeInt(config['ExpLevel'])   # ExpLevel
        self.writeInt(config['ExpPoints'])  # ExpPoints
        self.writeInt(config['Diamonds'])  # Diamonds
        self.writeInt(0)  # FreeDiamonds
        self.writeInt(0)  # AttackRating
        self.writeInt(0)  # AttackKFactor
        self.writeInt(config['Score'])  # Score
        self.writeInt(config['AttackWinCount'])  # AttackWinCount
        self.writeInt(config['AttackLoseCount'])  # AttackLoseCount
        self.writeInt(config['DefenseWinCount'])  # DefenseWinCount
        self.writeInt(config['DefenseLoseCount'])  # DefenseLoseCount
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeByte(0)  # NameSetByUser

        self.writeInt(0) # CumulativePurchasedDiamonds

        ##### ARAYS #####

        self.writeInt(0)#6) #array 1, resource cap data
        #self.writeInt(3000000)
        #self.writeInt(1000000)
        #self.writeInt(3000001)
        #self.writeInt(2000000000)
        #self.writeInt(3000002)
        #self.writeInt(2000000000)
        #self.writeInt(3000003)
        #self.writeInt(2000000000)
        #self.writeInt(3000007)
        #self.writeInt(2000000000)
        #self.writeInt(3000008)
        #self.writeInt(2000000000)
        
        self.writeInt(3) #array 2, resource data slot data
        # Gold
        self.writeInt(3000001)
        self.writeInt(1000000000) #gold
        # Elixir
        self.writeInt(3000002)
        self.writeInt(1000000000) #elixir
        # Dark Elixir
        self.writeInt(3000003)
        self.writeInt(1000000000) #darkelixir
        
        self.writeInt(0) #array 3, unit slot data
        self.writeInt(0) #array 4, spell slot data
        self.writeInt(0) #array 5, unit upgrade slot
        self.writeInt(0) #array 6, spell upgrade slot
        self.writeInt(0) #array 7, hero upgrade slot
        self.writeInt(0) #array 8, hero health slot
        self.writeInt(0) #array 9, hero state slot
        self.writeInt(0) #array 10, alliance unit data

        self.writeInt(0) #array 11, tutorial steps data

        self.writeInt(0) #array 12, achievement rewards data
        self.writeInt(0) #array 13, achievement progress data

        self.writeInt(50) #array 14, npc map progress data
        for i in range(17000000, 17000050):
            self.writeInt(i)
            self.writeInt(3)

        self.writeInt(0) #array 15, npc looted gold data
        self.writeInt(0) #array 16, npc looted elixir data

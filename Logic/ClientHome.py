import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))

starting_home = json.load(open("Gamefiles/level/starting_home.json", "r"))

class LogicClientHome(Writer):

    def encode(self):

        self.writeInt(0)

        if self.player.Major > 6 or (self.player.Major == 6 and self.player.Minor >= 253): # v6.253.x or above
            self.writeInt(0)

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeString(json.dumps(starting_home)) # HomeJSON

        self.writeInt(config['ShieldDurationSeconds'])  # ShieldDurationSeconds
        self.writeInt(0)  # DefenseRating
        self.writeInt(0)  # DefenseKFactor
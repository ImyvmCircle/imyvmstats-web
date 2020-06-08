import json
import os
from os.path import split

import nbtlib
from datetime import datetime

from web_project.settings import PDATA_ROOT, STATS_ROOT


class playersData():
    def __init__(self):
        super().__init__()
        self.players = list()
        self.loadData()
    
    def loadData(self):
        entries = os.listdir(PDATA_ROOT)
        for entry in entries:
            nbt_file = nbtlib.load(os.path.join(PDATA_ROOT, entry)).root["bukkit"]
            stats = dict()
            try:
                with open(os.path.join(STATS_ROOT, entry.split(".")[0]+".json"), "r") as f:
                    data = json.load(f)
                    if "stats" in data.keys():
                        stats = data["stats"]
            except:
                print("file not exist")
            self.players.append({
                "uuid": entry.split(".")[0],
                "firstPlayed": nbt_file["firstPlayed"]/1000,
                "lastKnownName": nbt_file["lastKnownName"],
                "lastPlayed": nbt_file["lastPlayed"]/1000,
                "stats": stats,
            })

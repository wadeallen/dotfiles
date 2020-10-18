import dmenu_extended
import sys
import requests
import datetime
import json
import zulu


r = requests.get('http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
data = r.json()

class extension(dmenu_extended.dmenu):

    # Set the name to appear in the menu
    title = 'NFL Scores'

    # Determines whether to attach the submenu indicator
    is_submenu = True


    # Required function, runs when the user fires the menu item
    def run(self, inputText):
        games = []
        for e in data["events"]:
            game = e["shortName"]
            games.append(game)
        
        self.menu(games)


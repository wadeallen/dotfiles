import dmenu_extended
import sys
import requests
import datetime
import json
import zulu
import pytz

r = requests.get('http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
data = r.json()

utc = pytz.UTC
local_tz = pytz.timezone('US/Eastern')
current_time = datetime.datetime.now().replace(tzinfo=pytz.utc).astimezone(local_tz)


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
            game_date = e["date"]
            dt = zulu.parse(game_date).datetime
            dt = dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
            team_home = e["competitions"][0]["competitors"][0]["team"]["shortDisplayName"]
            team_home = e["competitions"][0]["competitors"][0]["team"]["shortDisplayName"]
            score_home = int(e["competitions"][0]["competitors"][0]["score"])
            team_away = e["competitions"][0]["competitors"][1]["team"]["shortDisplayName"]
            score_away = int(e["competitions"][0]["competitors"][1]["score"])
            if current_time > dt:
                games.append(f"{team_home} {score_home} v {team_away} {score_away}")
            else:
                games.append(f"{game} at {dt.strftime('%a %-I:%M %p')}")
        self.menu(games)


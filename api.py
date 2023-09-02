import requests
import json
import pandas as pd

class static:
    def __init__(self):
        r = requests.get(
            'https://fantasy.premierleague.com/api/bootstrap-static/')
        self.data = json.loads(r.content)

    def get_events(self):
        events = pd.DataFrame(self.data['events'])
        events['id'] = events['id'].astype(str)
        return events

    def get_teams(self):
        teams = pd.DataFrame(self.data['teams'])
        teams['id'] = teams['id'].astype(str)
        teams['code'] = teams['code'].astype(str)
        return teams
    
    def get_elements(self):
        elements = pd.DataFrame(self.data['elements'])
        elements['id'] = elements['id'].astype(str)
        elements['code'] = elements['code'].astype(str)
        return elements

class fixtures:
    def __init__(self):
        r = requests.get('https://fantasy.premierleague.com/api/fixtures/')
        self.fixtures = pd.DataFrame(json.loads(r.content))
        self.fixtures['event'].fillna(0,inplace=True)
        self.fixtures['event'] = self.fixtures['event'].astype(str)
        self.fixtures['team_a'] = self.fixtures['team_a'].astype(str)
        self.fixtures['team_h'] = self.fixtures['team_h'].astype(str)
    
    def get_fixtures(self, is_finished=True):
        if is_finished:
            return self.fixtures.loc[self.fixtures['finished']]
        else:
            return self.fixtures.loc[self.fixtures['finished'] == False]
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
        self.fixtures['event'].fillna(0, inplace=True)
        self.fixtures['event'] = self.fixtures['event'].astype(str)
        self.fixtures['team_a'] = self.fixtures['team_a'].astype(str)
        self.fixtures['team_h'] = self.fixtures['team_h'].astype(str)

    def get_fixtures(self, is_finished=True):
        if is_finished:
            return self.fixtures.loc[self.fixtures['finished']]
        else:
            return self.fixtures.loc[self.fixtures['finished'] == False]


class elements:
    def __init__(self, id=1):
        r = requests.get(
            f'https://fantasy.premierleague.com/api/element-summary/{id}/')
        raw = json.loads(r.content)
        self.fixtures = pd.DataFrame(raw['fixtures'])
        convert_dict = {'id': str, 'code': str, 'team_h': str, 'team_a': str}
        self.fixtures = self.fixtures.astype(convert_dict)
        self.history = pd.DataFrame(raw['history'])
        convert_dict = {'element': str, 'fixture': str, 'opponent_team': str}
        self.history = self.history.astype(convert_dict)
        self.past_seasons = pd.DataFrame(raw['history_past'])


class gameweek:
    def __init__(self, id=1):
        r = requests.get(
            f'https://fantasy.premierleague.com/api/event/{id}/live/')
        raw = json.loads(r.content)
        id_list = []
        stats_list = []
        for player in raw['elements']:
            id_list.append(player['id'])
            stats_list.append(player['stats'])
        self.stats = pd.DataFrame(stats_list)
        self.stats.insert(0, 'id', id_list)

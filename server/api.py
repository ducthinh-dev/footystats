import requests
import json
import pandas as pd


class static:
    def __init__(self):
        r = requests.get(
            'https://fantasy.premierleague.com/api/bootstrap-static/')
        self.data = json.loads(r.content)

    def get_events(self, is_finished=False, is_current=False, is_next=False):
        events = pd.DataFrame(self.data['events'])
        events['id'] = events['id'].astype(str)
        if is_finished:
            return events.loc[events['finished']]
        if is_current:
            return events.loc[events['is_current']]
        if is_next:
            return events.loc[-events['finished']]
        return events

    def get_teams_info(self):
        teams = pd.DataFrame(self.data['teams'])
        teams['id'] = teams['id'].astype(str)
        teams['code'] = teams['code'].astype(str)
        return teams

    def get_elements_summary(self):
        elements = pd.DataFrame(self.data['elements'])
        convert_dict = {'id': str, 'code': str, 'element_type': str,
                        'team': str, 'team_code': str, 'selected_by_percent': float}
        elements = elements.astype(convert_dict)
        elements['now_cost'] = elements['now_cost'] * 0.1
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

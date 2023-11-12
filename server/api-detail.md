# fpl

# api

## api list

[https://fantasy.premierleague.com/api](https://fantasy.premierleague.com/api)

- static: /bootstrap-static/ → general events, teams, elements information
- fixtures: /fixtures/ → list of 380 fixtures in the season
- element summary: /element-summary/
- gameweek live: /event/{gameweek id}/live/ → list of detail info of each element in that gameweek

## api dictionaries

### static

- events
    
    ```json
    {'id': 1,
     'name': 'Gameweek 1',
     'deadline_time': '2023-08-11T17:30:00Z',
     'average_entry_score': 64,
     'finished': True,
     'data_checked': True,
     'highest_scoring_entry': 3383750,
     'deadline_time_epoch': 1691775000,
     'deadline_time_game_offset': 0,
     'highest_score': 127,
     'is_previous': False,
     'is_current': True,
     'is_next': False,
     'cup_leagues_created': False,
     'h2h_ko_matches_created': False,
     'chip_plays': [{'chip_name': 'bboost', 'num_played': 163222},
      {'chip_name': '3xc', 'num_played': 287198}],
     'most_selected': 355,
     'most_transferred_in': 1,
     'top_element': 395,
     'top_element_info': {'id': 395, 'points': 14},
     'transfers_made': 0,
     'most_captained': 355,
     'most_vice_captained': 19}
    ```
    
- teams
    
    ```json
    {'code': 3,
     'draw': 0,
     'form': None,
     'id': 1,
     'loss': 0,
     'name': 'Arsenal',
     'played': 0,
     'points': 0,
     'position': 0,
     'short_name': 'ARS',
     'strength': 4,
     'team_division': None,
     'unavailable': False,
     'win': 0,
     'strength_overall_home': 1230,
     'strength_overall_away': 1285,
     'strength_attack_home': 1250,
     'strength_attack_away': 1250,
     'strength_defence_home': 1210,
     'strength_defence_away': 1320,
     'pulse_id': 1}
    ```
    
- elements
    
    ```json
    {'chance_of_playing_next_round': 100,
     'chance_of_playing_this_round': 100,
     'code': 232223,
     'cost_change_event': 0,
     'cost_change_event_fall': 0,
     'cost_change_start': 0,
     'cost_change_start_fall': 0,
     'dreamteam_count': 0,
     'element_type': 4,
     'ep_next': '1.5',
     'ep_this': '1.5',
     'event_points': 0,
     'first_name': 'Folarin',
     'form': '0.0',
     'id': 1,
     'in_dreamteam': False,
     'news': '',
     'news_added': '2023-08-07T15:30:05.135490Z',
     'now_cost': 45,
     'photo': '232223.jpg',
     'points_per_game': '0.0',
     'second_name': 'Balogun',
     'selected_by_percent': '0.7',
     'special': False,
     'squad_number': None,
     'status': 'a',
     'team': 1,
     'team_code': 3,
     'total_points': 0,
     'transfers_in': 3077,
     'transfers_in_event': 3077,
     'transfers_out': 5374,
     'transfers_out_event': 5374,
     'value_form': '0.0',
     'value_season': '0.0',
     'web_name': 'Balogun',
     'minutes': 0,
     'goals_scored': 0,
     'assists': 0,
     'clean_sheets': 0,
     'goals_conceded': 0,
     'own_goals': 0,
     'penalties_saved': 0,
     'penalties_missed': 0,
     'yellow_cards': 0,
     'red_cards': 0,
     'saves': 0,
     'bonus': 0,
     'bps': 0,
     'influence': '0.0',
     'creativity': '0.0',
     'threat': '0.0',
     'ict_index': '0.0',
     'starts': 0,
     'expected_goals': '0.00',
     'expected_assists': '0.00',
     'expected_goal_involvements': '0.00',
     'expected_goals_conceded': '0.00',
     'influence_rank': 410,
     'influence_rank_type': 28,
     'creativity_rank': 410,
     'creativity_rank_type': 30,
     'threat_rank': 385,
     'threat_rank_type': 31,
     'ict_index_rank': 419,
     'ict_index_rank_type': 31,
     'corners_and_indirect_freekicks_order': None,
     'corners_and_indirect_freekicks_text': '',
     'direct_freekicks_order': None,
     'direct_freekicks_text': '',
     'penalties_order': None,
     'penalties_text': '',
     'expected_goals_per_90': 0,
     'saves_per_90': 0,
     'expected_assists_per_90': 0,
     'expected_goal_involvements_per_90': 0,
     'expected_goals_conceded_per_90': 0,
     'goals_conceded_per_90': 0,
     'now_cost_rank': 436,
     'now_cost_rank_type': 68,
     'form_rank': 460,
     'form_rank_type': 43,
     'points_per_game_rank': 460,
     'points_per_game_rank_type': 43,
     'selected_rank': 200,
     'selected_rank_type': 38,
     'starts_per_90': 0,
     'clean_sheets_per_90': 0}
    ```
    

### fixture

- fixture unfinished
    
    ```json
    {'code': 2367552,
     'event': None,
     'finished': False,
     'finished_provisional': False,
     'id': 15,
     'kickoff_time': None,
     'minutes': 0,
     'provisional_start_time': False,
     'started': None,
     'team_a': 6,
     'team_a_score': None,
     'team_h': 12,
     'team_h_score': None,
     'stats': [],
     'team_h_difficulty': 2,
     'team_a_difficulty': 2,
     'pulse_id': 93335}
    ```
    
- fixture finished
    
    ```json
    {'code': 2367540,
     'event': 1,
     'finished': True,
     'finished_provisional': True,
     'id': 2,
     'kickoff_time': '2023-08-12T12:00:00Z',
     'minutes': 90,
     'provisional_start_time': False,
     'started': True,
     'team_a': 16,
     'team_a_score': 1,
     'team_h': 1,
     'team_h_score': 2,
     'stats': 
    	//goals
    	[{'identifier': 'goals_scored',
       'a': [{'value': 1, 'element': 437}],
       'h': [{'value': 1, 'element': 13}, {'value': 1, 'element': 19}]},
    
    	//assists
      {'identifier': 'assists',
       'a': [{'value': 1, 'element': 378}],
       'h': [{'value': 1, 'element': 12}, {'value': 1, 'element': 20}]},
    
    	//own goals
      {'identifier': 'own_goals', 'a': [], 'h': []},
    
    	//penalties
      {'identifier': 'penalties_saved', 'a': [], 'h': []},
      {'identifier': 'penalties_missed', 'a': [], 'h': []},
    
    	//booked
      {'identifier': 'yellow_cards',
       'a': [{'value': 1, 'element': 453}, {'value': 1, 'element': 604}],
       'h': [{'value': 1, 'element': 29}, {'value': 1, 'element': 585}]},
      {'identifier': 'red_cards', 'a': [], 'h': []},
    	
    	//gk saves
      {'identifier': 'saves',
       'a': [{'value': 5, 'element': 28}],
       'h': [{'value': 1, 'element': 17}]},
      {'identifier': 'bonus',
       'a': [{'value': 2, 'element': 437}],
       'h': [{'value': 3, 'element': 19}, {'value': 2, 'element': 13}]},
    
    	//bonus points system
      {'identifier': 'bps',
       'a': [{'value': 26, 'element': 437},
        {'value': 20, 'element': 28},
        {'value': 17, 'element': 378},
        {'value': 14, 'element': 439},
        {'value': 10, 'element': 436},
        {'value': 10, 'element': 469},
        {'value': 9, 'element': 604},
        {'value': 8, 'element': 442},
        {'value': 8, 'element': 447},
        {'value': 8, 'element': 455},
        {'value': 4, 'element': 467},
        {'value': 3, 'element': 468},
        {'value': 2, 'element': 451},
        {'value': 2, 'element': 470},
        {'value': -2, 'element': 453}],
       'h': [{'value': 37, 'element': 19},
        {'value': 26, 'element': 13},
        {'value': 23, 'element': 12},
        {'value': 22, 'element': 20},
        {'value': 18, 'element': 15},
        {'value': 18, 'element': 540},
        {'value': 11, 'element': 6},
        {'value': 11, 'element': 14},
        {'value': 10, 'element': 17},
        {'value': 9, 'element': 25},
        {'value': 8, 'element': 26},
        {'value': 8, 'element': 29},
        {'value': 3, 'element': 585},
        {'value': 2, 'element': 5}]}],
    
     'team_h_difficulty': 2,
     'team_a_difficulty': 4,
     'pulse_id': 93322}
    ```
    

### gameweek live

- element
    
    ```json
    {'id': 313,
     'stats': {'minutes': 90,
      'goals_scored': 0,
      'assists': 0,
      'clean_sheets': 0,
      'goals_conceded': 1,
      'own_goals': 0,
      'penalties_saved': 0,
      'penalties_missed': 0,
      'yellow_cards': 0,
      'red_cards': 0,
      'saves': 0,
      'bonus': 0,
      'bps': 13,
      'influence': '20.0',
      'creativity': '0.5',
      'threat': '3.0',
      'ict_index': '2.4',
      'starts': 1,
      'expected_goals': '0.03',
      'expected_assists': '0.02',
      'expected_goal_involvements': '0.05',
      'expected_goals_conceded': '1.28',
      'total_points': 2,
      'in_dreamteam': False},
     'explain': [{'fixture': 9,
       'stats': [{'identifier': 'minutes', 'points': 2, 'value': 90}]}]}
    ```
    

### element summary

- fixtures
    
    ```json
    {'id': 30,
     'code': 2367567,
     'team_h': 17,
     'team_h_score': None,
     'team_a': 13,
     'team_a_score': None,
     'event': 3,
     'finished': False,
     'minutes': 0,
     'provisional_start_time': False,
     'kickoff_time': '2023-08-27T13:00:00Z',
     'event_name': 'Gameweek 3',
     'is_home': False,
     'difficulty': 2}
    ```
    
- history past
    
    ```json
    {'season_name': '2022/23',
     'element_code': 223094,
     'start_cost': 115,
     'end_cost': 124,
     'total_points': 272,
     'minutes': 2767,
     'goals_scored': 36,
     'assists': 9,
     'clean_sheets': 13,
     'goals_conceded': 26,
     'own_goals': 0,
     'penalties_saved': 0,
     'penalties_missed': 0,
     'yellow_cards': 5,
     'red_cards': 0,
     'saves': 0,
     'bonus': 40,
     'bps': 1040,
     'influence': '1390.0',
     'creativity': '371.0',
     'threat': '1825.0',
     'ict_index': '358.1',
     'starts': 33,
     'expected_goals': '28.54',
     'expected_assists': '3.11',
     'expected_goal_involvements': '31.65',
     'expected_goals_conceded': '25.24'}
    ```
    

# application
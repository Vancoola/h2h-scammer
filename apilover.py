import requests, json, datetime, time
from transliterate import translit


def country_def():
    url = "https://api-football-v1.p.rapidapi.com/v3/countries"

    headers = {
        "X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    request = requests.post("http://localhost:8000/api/country/", json=response.json()['response'])
    print(request.json())


def league_def():
    url = "https://api-football-v1.p.rapidapi.com/v3/countries"

    headers = {
        "X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    country = 2

    for i in response.json()['response']:
        for ii in requests.get('https://api-football-v1.p.rapidapi.com/v3/leagues',
                               headers={"X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
                                        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"},
                               params={"country": i['name']}).json()['response']:
            ii['league']['league_id'] = ii['league'].pop('id')
            try:
                ii['league']['slug'] = translit(ii['league']['name'], reversed=True).lower().replace(' ', '_').replace(
                    "'", '').replace('.', '') + '_' + i['name']
            except:
                ii['league']['slug'] = ii['league']['name'].lower().replace(' ', '_').replace("'", '').replace('.',
                                                                                                               '').replace(
                    '’', '').replace('/', '') + '_' + i['name']
            ii['league']['country'] = country
            # print(ii['league'])
            print(requests.post('http://localhost:8000/api/leagues/', json=ii['league']).json())
            print(ii['league']['slug'])
        country += 1


def league_and_seasons():
    url = "https://api-football-v1.p.rapidapi.com/v3/countries"

    headers = {
        "X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    country = 2

    for i in response.json()['response']:
        for ii in requests.get('https://api-football-v1.p.rapidapi.com/v3/leagues',
                               headers={"X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
                                        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"},
                               params={"country": i['name'], "current": "true"}).json()['response']:
            ii['league']['league_id'] = ii['league'].pop('id')
            try:
                ii['league']['slug'] = translit(ii['league']['name'], reversed=True).lower().replace(' ', '_').replace(
                    "'", '').replace('.', '') + '_' + i['name']
            except:
                ii['league']['slug'] = ii['league']['name'].lower().replace(' ', '_').replace("'", '').replace('.',
                                                                                                               '').replace(
                    '’', '').replace('/', '') + '_' + i['name']
            ii['league']['country'] = country
            # print(ii['league']['league_id'])
            ii['seasons'][0]['league'] = ii['league']['league_id']
            ii['seasons'][0]['events'] = ii['seasons'][0]['coverage']['fixtures'].pop('events')
            ii['seasons'][0]['lineups'] = ii['seasons'][0]['coverage']['fixtures'].pop('lineups')
            ii['seasons'][0]['statistics_fixtures'] = ii['seasons'][0]['coverage']['fixtures'].pop(
                'statistics_fixtures')
            ii['seasons'][0]['statistics_players'] = ii['seasons'][0]['coverage']['fixtures'].pop('statistics_players')
            ii['seasons'][0]['standings'] = ii['seasons'][0]['coverage'].pop('standings')
            ii['seasons'][0]['players'] = ii['seasons'][0]['coverage'].pop('players')
            ii['seasons'][0]['top_scorers'] = ii['seasons'][0]['coverage'].pop('top_scorers')
            ii['seasons'][0]['top_assists'] = ii['seasons'][0]['coverage'].pop('top_assists')
            ii['seasons'][0]['top_cards'] = ii['seasons'][0]['coverage'].pop('top_cards')
            ii['seasons'][0]['injuries'] = ii['seasons'][0]['coverage'].pop('injuries')
            ii['seasons'][0]['predictions'] = ii['seasons'][0]['coverage'].pop('predictions')
            ii['seasons'][0]['odds'] = ii['seasons'][0]['coverage'].pop('odds')
            ii['seasons'][0].pop('coverage')

            # print(ii['seasons'])
            # print()
            # print(requests.post('http://localhost:8000/api/leagues/', json=ii['league']).json())
            # print(requests.post('http://localhost:8000/api/seasons/', json=json.dumps(ii['seasons'][0])).json())
            # print(ii['seasons'][0])
            # print(ii['league']['slug'])
            print(ii)
            break
        break
        country += 1


def last():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    querystring = {"date": "2024-02-17"}

    headers = {
        "X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    for i in response.json()['response']:

        home_team = requests.get('https://api-football-v1.p.rapidapi.com/v3/teams',
                                 headers=headers, params={'id': str(i['teams']['home']['id'])}).json()['response'][0][
            'team']
        # try:

        home_team['team_id'] = home_team['id']

        away_team = requests.get('https://api-football-v1.p.rapidapi.com/v3/teams', headers=headers,
                                 params={'id': str(i['teams']['away']['id'])}).json()['response'][0]['team']
        print(away_team['country'])
        away_team['team_id'] = away_team['id']
        print(requests.post('http://localhost:8000/api/teams/', json=json.dumps(home_team)).json())
        print(requests.post('http://localhost:8000/api/teams/', json=json.dumps(away_team)).json())
        i['game_id'] = i['fixture'].pop('id')
        i['referee'] = i['fixture'].pop('referee')
        i['date'] = i['fixture'].pop('date')[:10]
        i['long'] = i['fixture']['status'].pop('long')
        i['short'] = i['fixture']['status'].pop('short')
        i['elapsed'] = i['fixture']['status'].pop('elapsed')
        i.pop('fixture')
        i['round'] = i['league'].pop('round')
        i['league'] = i['league'].pop('id')
        i['home'] = i['teams']['home']['id']
        i['away'] = i['teams']['away']['id']
        if i['teams']['home']['winner'] != None:
            i['winner'] = i['teams']['home'].pop('id')
        elif i['teams']['away']['winner'] != None:
            i['winner'] = i['teams']['away'].pop('id')
        else:
            i['winner'] = None
        i['home_goals'] = i['goals'].pop('home')
        i['away_goals'] = i['goals'].pop('away')
        print(requests.post('http://localhost:8000/api/games/', json=i).json())
        i['team'] = i['home']
        print(requests.post('http://localhost:8000/api/toplist/', json=i).json())
        i['team'] = i['away']
        print(requests.post('http://localhost:8000/api/toplist/', json=i).json())
        # print(i['team'])
        time.sleep(1)
    # break


def standings(league_id: str, team_id: str, season: str):
    resp = {}
    url = "https://api-football-v1.p.rapidapi.com/v3/standings"
    querystring = {"season": season, "league": league_id, "team": team_id}
    headers = {
        "X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    try:
        object = response.json()['response'][0]['league']['standings'][0][0]
    except IndexError:
        return {}
    resp['point'] = object['points']
    resp['goalsDiff'] = object['goalsDiff']
    resp['win'] = object['all']['win']
    resp['draw'] = object['all']['draw']
    resp['lose'] = object['all']['lose']
    resp['matches_played'] = object['all']['played']
    # print(object)
    print('\n\n', resp, '\n\n')
    return resp

def updater():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    headers = {
        "X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    leagues = requests.get('http://localhost:8000/api/leagues/').json()

    for league in leagues:
        toplist = {}
        games = {"league": league['league_id']}
        toplist['league'] = league['league_id']
        print(league['league_id'])
        querystring = {"league": str(league['league_id']), "season": league['season'], "last": "1"}

        response = requests.get(url, headers=headers, params=querystring)
        # print(response.json()['response'])
        try:
            i = response.json()['response'][0]
        except IndexError:
            continue
        print(i, end='\n\n\n')
        rounds = i['league']['round']
        i['league'] = league['league_id']
        i['home_teams'] = i['teams']['home']
        i['home_teams']['team_id'] = int(i['teams']['home']['id'])
        i['home'] = int(i['teams']['home']['id'])
        i['away_teams'] = i['teams']['away']
        i['away_teams']['team_id'] = int(i['teams']['away']['id'])
        i['away'] = int(i['teams']['away']['id'])
        print(i['home_teams'])
        print(i['away_teams'])
        print(requests.post('http://localhost:8000/api/teams/', json=json.dumps(i['home_teams'])).json(), end='\n\n')
        print(requests.post('http://localhost:8000/api/teams/', json=json.dumps(i['away_teams'])).json(), end='\n\n')
        # print(i, end='\n\n')
        if i['teams']['home']['winner']:
            games['winner'] = i['home']
        elif i['teams']['away']['winner']:
            games['winner'] = i['away']
        games['game_id'] = i['fixture']['id']
        games["home"] = i["home"]
        games["away"] = i["away"]
        games["date"] = i['fixture']['date'][:10]
        games["round"] = rounds
        print(games)
        print(requests.post('http://localhost:8000/api/games/', json=json.dumps(games)).json(), 'zx', end='\n\n')
        toplist['team'] = i['home']
        toplist['is_home'] = True
        toplist = dict(
            list(toplist.items()) + list(standings(league['league_id'], i['home'], league['season']).items()))
        print(requests.post('http://localhost:8000/api/toplist/', json=toplist).json(), end='\n\n')
        # toplist = {}
        toplist['league'] = league['league_id']
        toplist['team'] = i['away']
        toplist['is_home'] = False
        toplist['is_away'] = True
        toplist = dict(
            list(toplist.items()) + list(standings(league['league_id'], i['away'], league['season']).items()))
        print(requests.post('http://localhost:8000/api/toplist/', json=toplist).json(), end='\n\n')
        time.sleep(1)


updater()

# standings(43, 1828, 2023)
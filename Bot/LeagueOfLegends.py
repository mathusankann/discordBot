import requests
import json

LOLAPI = "?api_key=RGAPI-04cd12e5-a049-4809-a1be-5ab61cd791d7"
GETSUMMONER = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
GETCLASHTEAMID = "https://euw1.api.riotgames.com/lol/clash/v1/players/by-summoner/"


def find_summoner(name):
    x = requests.get(GETSUMMONER + name + LOLAPI)
    x.json()
    return x.content


def find_clash_team_by_summoner(name):
    summoner = json.loads(find_summoner(name))
    print(summoner['id'])
    clash_team_id = json.loads(requests.get(GETCLASHTEAMID + summoner['id'] + LOLAPI).json().content)
    print(clash_team_id)
    #clash_team = json.loads(requests.get(GETCLASHTEAMID + clash_team_id['teamId'] + LOLAPI).json().content)
    #print(clash_team.players)
    return "done"

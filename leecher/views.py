from __future__ import print_function
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from nba_py import player
from nba_py.player import get_player, PlayerNotFoundException
from nba_py.constants import *


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def playerinfo(request):
    template = loader.get_template('playerinfo.html')
    first_name = request.POST['player_first_name']
    last_name = request.POST['player_last_name']
    if not first_name:
        context = {
            "error": "First name is mandatory"
        }
        return HttpResponse(template.render(context, request))
    if not last_name:
        context = {
            "error": "Last name is mandatory"
        }
        return HttpResponse(template.render(context, request))

    try:
        plyr = get_player(first_name, last_name, just_id=False)
    except PlayerNotFoundException:
        context = {
            "error": "Player not found"
        }
        return HttpResponse(template.render(context, request))

    pc = player.PlayerSummary(plyr.iloc[0]['PERSON_ID'])
    player_stats = pc.headline_stats()

    context = {
        "player_id": plyr.iloc[0]['PERSON_ID'],
        "player_first_name": first_name,
        "player_last_name": last_name,
        "player_photo": "http://stats.nba.com/media/players/230x185/{}.png".format(plyr.iloc[0]['PERSON_ID']),
        "team_name": plyr.iloc[0]['TEAM_NAME'],
        "team_city": plyr.iloc[0]['TEAM_CITY'],
        "player_stats_timeframe": player_stats['TimeFrame'][0],
        "player_stats_pts": player_stats['PTS'][0],
        "player_stats_ast": player_stats['AST'][0],
        "player_stats_reb": player_stats['REB'][0],
        "player_stats_pie": player_stats['PIE'][0],
    }
    return HttpResponse(template.render(context, request))

#!/usr/bin/python
import sys


def get_sum(x, y):
    return x+y


def process_games(games):
    num_won = reduce(get_sum, map(lambda game_result: int(game_result[2]), games))
    num_draw = reduce(get_sum, map(lambda game_result: int(game_result[3]), games))
    num_lost = reduce(get_sum, map(lambda game_result: int(game_result[4]), games))
    num_scored = reduce(get_sum, map(lambda game_result: int(game_result[5]), games))
    num_conceded = reduce(get_sum, map(lambda game_result: int(game_result[6]), games))
    num_points = reduce(get_sum, map(lambda game_result: int(game_result[7]), games))
    return [num_won, num_draw, num_lost, num_scored, num_conceded, num_points]


def get_scored_conceded(a_list):
    return [str(a_list[3]) + ":" + str(a_list[4])]


def process_team_games(teamgames):
    team = teamgames[0][0]
#     [team, where, win, draw, lose, goals_scored, goals_conceded, points]
    home_games = filter(lambda a_game: a_game[1] == "home", teamgames)
    away_games = filter(lambda a_game: a_game[1] == "away", teamgames)
    num_played = str(len(teamgames))

    home_results = [h_num_won, h_num_draw, h_num_lost, h_num_scored, h_num_conceded, h_num_points] = process_games(home_games)
    away_results = [a_num_won, a_num_draw, a_num_lost, a_num_scored, a_num_conceded, a_num_points] = process_games(away_games)
    total_scored = h_num_scored + a_num_scored
    total_conceded = h_num_conceded + a_num_conceded
    total_points = h_num_points + a_num_points

    printable = [team, num_played]
    printable.extend(home_results[:3])
    printable.extend(get_scored_conceded(home_results))
    printable.extend(away_results[:3])
    printable.extend(get_scored_conceded(away_results))
    printable.extend([str(h_num_scored+a_num_scored)+":"+str(h_num_conceded+a_num_conceded)])
    printable.extend([str(total_scored-total_conceded), str(total_points)])
    print "\t".join(map(lambda col: str(col), printable))


current_team = None
games_of_a_team = []
# for line in open("mapper_output.txt","r"):
for line in sys.stdin:
    [team, where, win, draw, lose, goals_scored, goals_conceded, points] = line.strip().split("\t")
    if not current_team:
        current_team = team
    if team == current_team:
        games_of_a_team.append([team, where, win, draw, lose, goals_scored, goals_conceded, points])
    else:
        process_team_games(games_of_a_team)
        current_team = team
        games_of_a_team = []
process_team_games(games_of_a_team)

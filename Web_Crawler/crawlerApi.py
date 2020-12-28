from game_info import GameInfo
from crawler import extract_dates_from_file, extract_games_from_file, extract_times_from_file, extract_odds_from_file


def read_file(path="../sample2.txt",start = 0 ,end = -1):
    f = open(path, "rb")
    return f.readlines()[0][start:end]


file_content = read_file()
games = extract_games_from_file(file_content)
dates = extract_dates_from_file(file_content)
times = extract_times_from_file(file_content)
odds = extract_odds_from_file(file_content)
home_teams = games[0:][::2]
guest_teams = games[1:][::2]


date_index = 0
index = 0
games = []
while index < len(home_teams):
    if date_index < len(dates)-1:
        if home_teams[index]['index'] > dates[date_index+1]['index']:
            date_index = date_index+1
    temp_game = GameInfo(home_teams[index]['data'], guest_teams[index]['data'], dates[date_index]['data'], times[index]['data'], odds[0][index], odds[1][index], odds[2][index])
    games.append(temp_game)
    index = index + 1
for game in games:
    print(game)


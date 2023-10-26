import soccerdata as sd

fbref2122 = sd.FBref('GER-Bundesliga', '2122')
games = fbref2122.read_team_match_stats(stat_type = 'shooting')
print(games.head())

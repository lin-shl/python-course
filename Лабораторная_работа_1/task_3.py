list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

amount_players = len(list_players)
in_between = amount_players // 2

team_1 = list_players[:in_between]
team_2 = list_players[in_between:]

print(f'{team_1}\n{team_2}')

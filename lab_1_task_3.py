list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)

# Выше записано предложенное курсом решение. Ниже запишу свое
# Условия, как нужно разделять на команды, не было
# Сказано: на две равные команды, поэтому можно поступить так:
count_players = len(list_players)
team1 = list_players[0:count_players:2]
team2 = list_players[1:count_players:2]
print(team1)
print(team2)
# Условию задания результат удовлетворяет
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money = money_capital+salary
count = 0
while spend<money:
    money-= spend
    spend = (increase+1)*spend
    count+=1
    money+=salary
print("Количество месяцев, которое можно протянуть без долгов:", count)

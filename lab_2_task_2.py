import math
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен (было дано изначально в тексте программы)
#increase = 0.05 # Ежемесячный рост цен (по заданию)
money = 0
for _ in range(months):
    money = money - spend + salary
    spend = spend * (1 + increase)
money=math.ceil(abs(money))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money)

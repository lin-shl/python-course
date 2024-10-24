money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

while spend <= money_capital + salary:
    # Первый месяц без повышения цен, поэтому:
    if month != 0:
        spend += spend * increase

    money_capital -= spend
    money_capital += salary
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
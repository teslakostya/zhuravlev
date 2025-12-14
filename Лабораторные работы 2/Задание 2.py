salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
shortfall = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for month in range(months):
    if month > 0:
        spend *= (1 + increase)

    shortfall = spend - salary
    if shortfall > 0:
        money_capital += shortfall

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",round(money_capital))
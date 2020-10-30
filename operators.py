money = 50000
countDay = 30
expensesOne = 200
expensesTwo = 1000
mission = 100000

expensesMonth = expensesOne + expensesTwo
budgetMonth = money - expensesMonth
budgetDay = budgetMonth / countDay
period = mission / budgetMonth

# накопления за неделю (с учетом выходных)
print(budgetDay * 5)

# накопления за неделю (для трудоголиков)
print(budgetDay * 7)

# оклад с премией
print(money + 5000)

# оклад с премией (для трудоголиков)
print(money + 6000)

# оклад с учетов штрафа
print(money - 500)

# для задания пара примеров других операторов
print(3 ** 3)
print(6 % 5)
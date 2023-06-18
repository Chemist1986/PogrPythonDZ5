names = ['Антон', 'Владимир', 'Анастасия']
rates = [1000, 2000, 1500]
bonuses = ['10.25%', '5%', '8.5%']

result = {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}
print(result)

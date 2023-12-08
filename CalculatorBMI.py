h = int(input('Ваш рост (см): ')) / 100
w = int(input('Ваш вес (кг): '))
BMI = w/h/h
print(f'Ваш индекс массы тела: {round(BMI, 2)}')
i = round(BMI)
l, r = 20, 50
print(str(l) + '='*(i-l-1) + '|' + '='*(r-i-1) + str(r))


# можно было бы использовать фукнкцию:
# def calc_sum_digits(cube):
# 	sum_of_numbers = 0
# 	while cube:
# 		n = cube % 10
# 		cube = cube // 10
# 		sum_of_numbers += n
# 	if not sum_of_numbers % 7:
# 		return sum_of_numbers
# 	else:
# 		return 0

a = []
total1 = 0
total2 = 0

# вместо цикла для создания списка использую генератор (ниже)
# for i in range(1,1001):
# 	if i % 2:
# 		a.append(i ** 3)

# здесь использую генератор списка для создания списка 
a = [i ** 3 for i in range(1,1001) if i % 2]

for i in a:
	# Нижние две строчки для варианта с функцией (закомментировано)
	# total1 += calc_sum_digits(i)
	# total2 += calc_sum_digits(i + 17)
	cube = i
	sum_of_numbers = 0
	while cube:
		n = cube % 10
		cube = cube // 10
		sum_of_numbers += n
	if not sum_of_numbers % 7:
		total1 += sum_of_numbers
	cube = i + 17
	sum_of_numbers = 0
	while cube:
		n = cube % 10
		cube = cube // 10
		sum_of_numbers += n
	if not sum_of_numbers % 7:
		total2 += sum_of_numbers

print('Результат задания из пункта a: ', total1)
print('Результат задания из пункта b: ', total2)
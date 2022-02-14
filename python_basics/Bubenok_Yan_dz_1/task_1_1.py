duration = [112987, 89456, 34098]

for last in duration:

	d = last // 86400
	h = last // 3600 % 24
	m = last // 60 % 60
	s = last % 60
	
	time = ""
	if d > 0:
		time += str(d) + " дн "
	if h > 0:
		time += str(h) + " час "
	if m > 0:
		time += str(m) + " мин "
	if s > 0:
		time += str(s) + " сек "
	print("duration = ", last)
	print(time)
	# или можно собрать дату через f-строку
	# print(f'{d} д {h} ч {m} мин {s} сек')


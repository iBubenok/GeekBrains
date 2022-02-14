for i in range(1,101):
	if 10 < i < 15:
		word_declension = 'процентов'
	elif i % 10 == 1:
		word_declension = 'процент'
	elif 1 < i % 10 < 5:
		word_declension = 'процента'
	else:
		word_declension = 'процентов'
	print(i, word_declension)
	
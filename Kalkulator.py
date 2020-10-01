while True:
	x = float(input('podaj liczbe x: '))
	y = float(input('podaj liczbe y: '))
	print('x=',x)
	print('y=',y)

	print("jesli chcesz dodac, kliknij 1")
	print("jesli chcesz odjac, kliknij 2")
	print("jesli chcesz pomnozyc, kliknij 3")
	print("jesli chcesz podzielic, kliknij 4")
	print("jesli chcesz wyjsc, kliknij 5")

	liczba = int(input('podaj liczbe: '))
	if liczba == 1:
		print('wynik dodawania to: ', x + y)
		
	if liczba == 2:
		print('wynik odejmowania to: ', x - y)
		
	if liczba == 3:
		print('wynik mnozenia to: ', x * y)
	
	if liczba == 4:
		if y == 0:
			print('nie dzielimy przez zero')
			break
		print('wynik dzielenia to: ', x / y)
		
		
	if liczba == 5:
		break 
			
	else:
		print('nieprawidlowe dzialanie')
		continue
	

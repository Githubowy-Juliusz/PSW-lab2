import random, statistics
list_of_available_values = [2, 3, 3.5, 4, 4.5, 5]
print('''Napisz "exit", by zamknąć program.''')
while True:
	received_line = input("Wprowadź długość tablicy.\n")
	if received_line.lower() == "exit":
		break
	try:
		length_of_list = int(received_line)
		if length_of_list > 0:
			random_list = []
			while length_of_list > 0:
				random_integer = random.randint(0, len(list_of_available_values) - 1)
				random_value_from_list = list_of_available_values[random_integer]
				random_list.append(random_value_from_list)
				length_of_list -= 1
			print("Wylosowana tablica: " + str(random_list))
			average = statistics.mean(random_list)
			minimum = min(random_list)
			maximum = max(random_list)
			standard_deviation = 0.0
			try:
				standard_deviation = statistics.stdev(random_list)
			except:
				pass
			print("Średnia: " + str(average))
			print("Wartość minimalna: " + str(minimum))
			print("Wartość maksymalna: " + str(maximum))
			print("Odchylenie standardowe: " + str(standard_deviation))
		else:
			print("Długość nie może być zerowa.")
	except:
		print("To nie jest liczba całkowita.")

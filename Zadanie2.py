import numpy

def matrix_operations():
	print('''Napisz "exit", by zamknąć program.''')
	while True:
		size = 0
		while size == 0:
			received_line = input("Wprowadź rozmiar macierzy.\n")
			if received_line.lower() == "exit":
				return
			try:
				size = int(received_line)
				if size == 0:
					print("Rozmiar nie może być zerowy.")
			except:
				print("To nie jest liczba całkowita.")
		matrix_a = numpy.random.rand(size, size) * 20 - 10
		matrix_b = numpy.random.rand(size, size) * 20 - 10
		matrix_addition = matrix_a + matrix_b
		matrix_a_subtract_b = matrix_a - matrix_b
		matrix_b_subtract_a = matrix_b - matrix_a
		matrix_multiplication = numpy.matmul(matrix_a, matrix_b)
		print("Pierwsza macierz:\n" + str(matrix_a))
		print("Druga macierz:\n" + str(matrix_b))
		print("Dodawanie macierzy:\n" + str(matrix_addition))
		print("Odejmowanie macierzy (A-B):\n" + str(matrix_a_subtract_b))
		print("Odejmowanie macierzy (B-A):\n" + str(matrix_b_subtract_a))
		print("Mnożenie macierzy:\n" + str(matrix_multiplication))

matrix_operations()

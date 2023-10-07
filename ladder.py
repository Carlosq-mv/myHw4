def my_steps(n:int):
	try:
		if n > 25 or n < 1:
			raise ValueError
	except ValueError as error:
		return error

	if n == 1 or n == 0:
		return 1
	previous, current = 1, 1
	for i in range(2, n+1):
		temp = current
		current = previous + current
		previous = temp
	return current


print(my_steps(26))
def my_steps(n:int):
	if n > 25 or n < 1:
		raise ValueError
	else:
		if n == 1 or n == 0:
			return 1
		previous, current = 1, 1
		for i in range(2, n+1):
			temp = current
			current = previous + current
			previous = temp
		return current

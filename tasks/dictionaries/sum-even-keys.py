def sum_even_keys(my_dictionary):
	total = 0
	for key, value in my_dictionary.items():
		if key % 2 == 0:
			total += value

	return total


print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))

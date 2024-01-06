def max_key(my_dictionary):
	max_value = float('-inf')

	for key, value in my_dictionary.items():
		if value > max_value:
			max_value = value
			max_key = key

	return max_key


print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))

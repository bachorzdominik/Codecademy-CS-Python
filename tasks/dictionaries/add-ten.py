def add_ten(my_dictionary):
	return {key:value+10 for key, value in my_dictionary.items()}


print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))

def values_that_are_keys(my_dictionary):
	val_key = []
	values = my_dictionary.values()
	keys = my_dictionary.keys()

	for v in values:
	 	if v in keys:
	 		val_key.append(v)

	return val_key


print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

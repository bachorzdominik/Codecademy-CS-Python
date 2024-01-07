def unique_values(my_dictionary):
	unique = []
	for value in my_dictionary.values():
		if value not in unique:
			unique.append(value)

	return len(unique)


print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))

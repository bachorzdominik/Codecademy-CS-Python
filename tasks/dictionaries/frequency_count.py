def frequency_dictionary(words):
	frequency = {}
	for word in words:
		if word in frequency:
			frequency[word] += 1
		else:
			frequency[word] = 1

	return frequency


print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))

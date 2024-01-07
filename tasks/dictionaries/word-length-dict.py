def word_length_dictionary(words):
		for word in words:
			result = {key: len(key) for key in words}

		return result


print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))

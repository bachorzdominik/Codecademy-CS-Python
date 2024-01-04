def x_length_words(sentence, x):
	words = sentence.split()
	for w in words:
		if len(w) < x:
			return False

	return True


print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))

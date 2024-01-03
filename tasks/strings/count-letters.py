def unique_english_letters(word):
	used_letters = []

	idx = 0
	for letter in word:
		if letter not in used_letters:
			used_letters.append(letter)
			idx += 1

	return idx


print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))

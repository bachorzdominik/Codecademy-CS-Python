def count_char_x(word, x):
	idx = 0
	for ch in word:
		if ch == x:
			idx += 1

	return idx


print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

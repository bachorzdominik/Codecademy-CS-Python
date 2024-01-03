def substring_between_letters(word, start, end):
	try:
		return word[word.index(start)+1:word.index(end)]
	except ValueError:
		return word


print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))

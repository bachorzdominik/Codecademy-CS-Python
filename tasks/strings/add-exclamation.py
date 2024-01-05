#1
def add_exclamation1(word):
	word_len = len(word)
	exclamations = word_len * '!'

	if word_len < 20:
		return f'{word}{exclamations}'
	else:
		return word


#2
def add_exclamation2(word):
	while len(word) < 20:
		word += '!'
	return word


print(add_exclamation1("Codecademy"))
print(add_exclamation1("Codecademy is the best place to learn"))

print(add_exclamation2("Codecademy"))
print(add_exclamation2("Codecademy is the best place to learn"))

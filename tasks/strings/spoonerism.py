#1
def make_spoonerism1(word1, word2):
	w1 = word1.replace(word1[0], word2[0])
	w2 = word2.replace(word2[0], word1[0])

	return f'{w1} {w2}'


#2
def make_spoonerism2(word1, word2):
	w1 = word2[0] + word1[1:]
	w2 = word1[0] + word2[1:]

	return f'{w1} {w2}'


print(make_spoonerism1("Codecademy", "Learn"))
print(make_spoonerism1("Hello", "world!"))
print(make_spoonerism1("a", "b"))


print(make_spoonerism2("Codecademy", "Learn"))
print(make_spoonerism2("Hello", "world!"))
print(make_spoonerism2("a", "b"))

def count_first_letter(names):
	first_letters = {}
	for key, value in names.items():
		if key[0] in first_letters:
			first_letters[key[0]] += len(value)
		else:
			first_letters[key[0]] = len(value)

	return first_letters


print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))

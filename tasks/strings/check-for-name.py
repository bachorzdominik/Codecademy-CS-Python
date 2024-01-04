def check_for_name(sentence, name):
	if name.lower() in sentence.lower():
		return True
	return False


print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is JAMIE", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))

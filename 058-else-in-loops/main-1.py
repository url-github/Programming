words_list = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "pear", "abort",
    "plum", "quince", "raspberry", "strawberry", "tangerine",
    "watermelon", "apricot", "blueberry", "cantaloupe", "dragonfruit",
    "grapefruit", "jackfruit", "kumquat", "lime", "melon"
]


wordsAppend = []

for word in words_list:
	print("Dodawanie kolejnego elementu", word)
	wordsAppend.append(word)

	if word == "abort":
		print(f"Przerwanie pętli, bo trafiłem na \"abort\"")
		wordsAppend.clear()
		break

else:
	print(wordsAppend)


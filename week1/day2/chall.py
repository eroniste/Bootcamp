def letter_indexes():
    word = input("Enter a word: ").strip()
    letter_dict = {}

    for index, letter in enumerate(word):
        if letter in letter_dict:
            letter_dict[letter].append(index)
        else:
            letter_dict[letter] = [index]

    print(letter_dict)

letter_indexes()

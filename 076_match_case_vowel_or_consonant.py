print("Please enter an alphabet: ")
MY_ALPHABET = input()[0]

MY_ALPHABET_LOWER_CASE = MY_ALPHABET.lower()

match MY_ALPHABET_LOWER_CASE:
    case 'a'|'e'|'i'|'o'|'u':
        print(f"Alphabet: {MY_ALPHABET} is a vowel.")
    case _:
        print(f"Alphabet: {MY_ALPHABET} is a consonant.")

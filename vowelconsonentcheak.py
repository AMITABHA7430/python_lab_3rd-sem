ch = input("Enter a character: ").lower()

if len(ch) != 1:
    print("Please enter a single character")
elif not ch.isalpha():
    print("Please enter an alphabet character")
elif ch in "aeiou":
    print(ch, "is a VOWEL")
else:
    print(ch, "is a CONSONANT")

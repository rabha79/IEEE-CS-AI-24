word = input("enter a word:")
reverse = word[::-1]
if word == reverse:
    print(f"the word {word} is palindrome")
else:
    print("it not a palindrome")
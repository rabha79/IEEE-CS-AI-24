word = input("enter sentence: ")
index = word.index(" ")
last = word[index+1:]
first = word[0:index]
print(f"{last} {first}")

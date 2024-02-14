# Create a program that reads a text file,
# counts the occurrences of each word, and prints the results.
import os
counts = {}
try:
    with open("Sample.txt", 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.,?!:;\'"()[]{}').lower()
                counts[word] = counts.get(word, 0) + 1
    for word, count in counts.items():
        print(f"{word}: {count}")
except FileNotFoundError:
    print("File not found!")

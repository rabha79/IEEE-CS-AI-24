# Write a function that takes two sets as input and returns a new set containing
# the common elements.

def common(first,second):
    common = first.intersection(second)
    return common


first = {"apple", "orange", "banana", "coconut"}
second = {"apple", "pineapple", "banana", "kiwi"}
result = common(first, second)
print(result)
numbers = input("enter any numbers: ")
if numbers.find('-1'):
    numbers = [int(x) for x in numbers.split()]
    num = numbers[0:-1]
    large = max(num)
    small = min(num)
    print(f"{large} {small}")
else:
    print("")






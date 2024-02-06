number = int(input("enter a number: "))
sum=0
for x in range (1,number):
    if(number % x == 0):
        sum += x
if(sum == number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")

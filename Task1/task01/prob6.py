num = int(input("enter a number: "))
sum=0
for x in range(2, num+1, 2):
    sum += x
print(f"The sum of even numbers from 1 to {num} is {sum}")

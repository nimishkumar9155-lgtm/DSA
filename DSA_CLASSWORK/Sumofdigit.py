# find the sum of all digits number given by user.

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10      
    sum = sum + digit  
    num = num // 10 

print("Sum of digits = ", sum)
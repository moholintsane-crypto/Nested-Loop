#take two input from user
val1= int(input("enter the first number for the range: "))
val2 = int(input("enter the second number for the range: "))
lower = min(val1, val2)
upper = max(val1, val2)
print("Prime numbers between", lower, "and", upper, "are:")
#iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
    if is_prime:
        print(num)
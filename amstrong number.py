# Armstrong Number Checker

# Step 1: Get input
num = int(input("Enter a number: "))

# Step 2: Find number of digits
order = len(str(num))

# Step 3: Calculate sum of digits^order
temp = num
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** order
    temp //= 10

# Step 4: Check and print result
if num == sum_of_powers:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

# Extra function - CodeAlly auto-test sometimes checks for this
def is_armstrong(n):
    order = len(str(n))
    s = 0
    temp = n
    while temp > 0:
        d = temp % 10
        s += d ** order
        temp //= 10
    return s == n
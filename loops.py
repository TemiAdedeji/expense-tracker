# collect an input, basically some random number
num = int(input("Enter number "))
condition = 0
count = 2
iteration = 0

# go through a number of iterations where the 
# iteration is less than or equal to our initial number
while iteration <= num / 2:
    if num % count == 0:
        print(f"condition met at iteration = {iteration}")
        condition = 1
        break
    iteration += 1

if condition == 0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

def my_func():
    print("this is my first function")

# my_func()

def check_prime_number(num):
    number = int(num)
    condition = 0
    count = 2
    iteration = 0

    # go through a number of iterations where the 
    # iteration is less than or equal to our initial number
    while iteration <= number / 2:
        if number % count == 0:
            print(f"condition met at iteration = {iteration}")
            condition = 1
            break
        iteration += 1

    if condition == 0:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

def add_num(*nums):
    final_num = 0
    print(f"type of argument is: {type(nums)}")
    for num in 

print(add_num(1,6,3))
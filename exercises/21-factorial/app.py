# Your code here
def factorial(fact):
    total = 1
    counter = fact
    for i in range(0,fact):
        total = total * counter
        counter += -1
    return total

print(factorial(8))
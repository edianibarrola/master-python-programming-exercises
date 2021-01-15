#Complete the function to return the tens digit of a given interger
def tens_digit(num):
    numstring = str(num)
    numstring = numstring[-2:]
    numstring = numstring[:1]
    return int(numstring)




#Invoke the function with any interger.
print(tens_digit(854345))
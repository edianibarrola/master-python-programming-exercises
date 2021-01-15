#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
    numstring = str(num)
    num1 = numstring[:1]
    num2 = numstring[1: len(numstring)-1:]
    num3 = numstring[2:len(numstring):]
    return  int(num1) + int(num2) + int(num3)


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))
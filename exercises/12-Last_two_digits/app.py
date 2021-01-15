#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):
    if num > 9:
        stringnum= str(num)
        last_two= stringnum[slice( len(stringnum)-2, len(stringnum))]
    return int(last_two)

#Invoke the function with any interger greater than 9.
print(last_two_digits(30))

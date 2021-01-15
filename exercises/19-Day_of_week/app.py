#Complete the function to return the number of day of the week for k'th day of year. 
# 0 -sunday ....  6- saturday
def day_of_week(k):
    daycounter = 4
    for days in range(1,k):

        if daycounter != 6:
            daycounter += 1
        else: daycounter = 0
            
        


    return daycounter



#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(56))
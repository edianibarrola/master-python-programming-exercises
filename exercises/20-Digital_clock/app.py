#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
    number_of_minutes = n
    hours = number_of_minutes // 60
    minutes = number_of_minutes % 60


    return hours, minutes

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))

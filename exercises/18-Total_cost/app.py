#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    dollars = int(d)
    cents = int(c)
    cupcakes = int(n)
    total_amount_dollars = 0
    total_amount_cents = 0

    total_amount_dollars = int((dollars*100 + c // 100)/100 * cupcakes)
    total_amount_cents = int((cents % 100)* cupcakes)

    return total_amount_dollars, total_amount_cents
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(15,22,4))

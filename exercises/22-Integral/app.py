
def integral(n):
    integral_dict = {}
    
    for i in range(1, n+1):
        integral_dict.__setitem__(i, i*i)
        
        i = i + 1
    
    return integral_dict

print(integral(6))
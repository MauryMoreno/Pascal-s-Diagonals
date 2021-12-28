def generate_diagonal(n, l):
    # return an array containing the numbers in the nth diagonal of Pascal's triangle, to the specified length  
    data=[]
    for i in range(n,n+l):   
        data.append(combinatoria(i,n))   
    return data
 

def combinatoria(n,x):
    comb=factorial(n)//(factorial(x)*factorial(n-x))
    return comb

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    return fact
  
'''this is a very fast way of
computing the nth value of the
fibonacci sequence.
It does so using the 'cache'
decorator imported from the 
functools library.
'''
from functools import cache

@cache          #cache each value as they are computed
def fib(n):     #defines the function 'fib'
    if n <= 1:      #starting point
        return n
    return fib(n-1) + fib(n-2)      #calculate fib as the last number added to it's previous number

for i in range (500):       #using a range of 500
    print(i, fib(i))        #print out the number and the i'th fibonacci number
print("done")               #lets user know it has finished the loop

'''even though we are using an inefficient definition,
cache is 'remembering' all of the values of the function
it has computed before.
'''

'''you could replace @cache (which remembers all of the previous calculations)
with @lru_cache(maxsize=5)  which will retain only the previous 5 computations
'''
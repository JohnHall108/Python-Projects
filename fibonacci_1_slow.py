'''this is a very slow way of
computing the nth value of the
fibonacci sequence.
It does so in a recursive fashion
so it's completely inefficient.
'''

def fib(n):     #defines the function 'fib'
    if n <= 1:      #starting point
        return n
    return fib(n-1) + fib(n-2)      #calculate fib as the last number added to it's previous number

for i in range (500):       #using a range of 500
    print(i, fib(i))        #print out the number and the i'th fibonacci number
print("done")               #lets user know it has finished the loop

#each number takes twice as long to compute as the number before it
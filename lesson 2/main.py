

n=int(input('What number of the Fibonacci Series would you like to know? '))

num=0
num1=1
next=1
sum=0
for i in range(num1,n-1):
    num=num1
    num1=next
    next=num+num1

print(next)


#recursion

def fib(n):
    if n == 0 or n ==1:
        return n
    else:
        return fib(n-1)+fib(n-2)  # <---recursion
    
print(fib(7))
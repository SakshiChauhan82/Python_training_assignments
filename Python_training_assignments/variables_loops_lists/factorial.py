# factorial
print("Factorial using iteration and recursion")
n = int(input("Enter a number"))

# using iteration
factorial=1
for i in range(1,n+1):
    factorial*=i
print("factorial using iteration")
print(factorial)

# using recursion
 
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print("factorial using recursion")
print(fact(n))

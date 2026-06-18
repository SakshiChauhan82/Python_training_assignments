print("Number guessing game")
import random
list1 = []
num = 18
n = int(input("Enter no. of attempts"))
for i in range(n):
    a = random.randint(1,100)
    print(a)
    list1.append(a)
    if a>num:
        print("Too high")
    elif a<num:
        print("Too low")
    else:
        print("Correct guess")
        print("Number to attempts taken to guess correctly",i)
        break
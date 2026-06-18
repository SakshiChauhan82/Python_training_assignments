print("Smart ATM simulator")

total_amt = int(input("Enter account balance"))
choice = int(input("Enter choice "))
t_history = [] 
t_history.append(total_amt)
if choice == 1:
    print(" Account Balance - ", total_amt)
elif choice == 2:
    amt = int(input("enter amount to withdraw"))
    if total_amt - amt >= 10000:
        print("withhdraw money - ", amt)
        total_amt-amt
        t_history.append(total_amt-amt)
        print("Account Balance - ", total_amt-amt)
        print("transaction History", t_history)
    else:
        print("Insufficient balance")
elif choice ==3:
    deposit= int(input("Enter amount to deposit"))
    total_amt+deposit
    t_history.append(total_amt+deposit)
    print("Depositied amount", deposit)
    print(" Account Balance - ", total_amt+deposit)
    print("transaction History", t_history)
else:
    print("Exit")

    



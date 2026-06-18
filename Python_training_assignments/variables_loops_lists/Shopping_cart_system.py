print("Shopping cart system")
cart =[]
choice = input("Enter choice  ")

if choice == "1": # add product
    addp = input("Enter the producct nam that you want to add  ")
    cart.append(addp)
elif choice == "2": # remove product
    rem = input("Enter the producct nam that you want to remove  ")
    cart.remove(rem)
elif choice == "3": # view products
    print("no. of products in the cart - ", len(cart))
    print("product list - ",cart)
else:
    print("Exit")
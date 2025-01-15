menu = {
    'pizza' : 70,
    'coffee' : 50,
    'pasta' : 40,
    'burger' : 35,
    'salad' : 60,
}
print("Welcome to our restaurant. Here's the menu:")
print("Pizza : Rs70\nCoffee : Rs50\nPasta : Rs40\nBurger : Rs35\nSalad : Rs60")
order = input("Enter the first item you want to order:")
bill = 0
if order in menu.keys():
    bill += menu[order]
    print(f"Order of {order} has been added")
    nextOrder = input("Do you want to order anything else?")
    if nextOrder == "yes" or nextOrder == "Yes":
        secOrder = input("Enter the second item you want to order:")
        bill += menu[secOrder]
        print("The total price to pay is:",bill)
    else:
        print("The total price to pay is:",bill)
else:
    print("Item is not available")
    

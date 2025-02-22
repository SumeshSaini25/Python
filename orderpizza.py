print("*" *25)
print("    Margherita pizza")
print("*"*25)
m = ['yes','no']
bill = 0
Menu = {'Wine' : 1500,
        'Per Slice ' : 110,
        'Garlic Bread': 80,
        'Special service' : 50}
for i , k in Menu.items():
    print(f"{i} : {k}")

slices = int(input("How many slices can we get for you : "))
prices=slices*Menu["Per Slice "];bill+=prices
wine = int(input("How many glasses of  wine : "))
pricew = wine*Menu["Wine"];bill+=pricew
Garlic = int(input("How many Garlic bread can we get for you : "))
priceg = Garlic*Menu["Garlic Bread"];bill+=priceg
scharges = 0
while True:
    service = input("Do you want special services yes or no :").lower()
    if service not in m: print("Invalid")
    else:
        if service == 'yes':
            bill+=Menu["Special service"];scharges+=Menu['Special service']
            break
        elif service == 'no':
            break

            
print(f"Your Total bill {bill}\nPizza {prices}\nWine {pricew}\nGarlic Bread {priceg}\nSpecial Services {scharges}")
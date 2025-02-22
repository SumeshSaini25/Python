import sys
print("*" *25)
print("        WELCOME")
print("*"*25)
height = float(input("Enter your height : "))
bill = 0
if height>= 120 :
    age = int(input("Enter your age : "))
    if age <=0 : print("Enter a valid age")
    elif age <=10: bill =55
    elif age <=15: bill = 80
    elif age in range(45,56): print("Its ok ride is on us");bill+=0
    else: bill = 115

    pics = input("Do you want to click your memories yes or no : ").lower()
    if pics != "yes" and pics !="no" : print("Ivalid input");sys.exit()
    if pics == 'yes' : bill+=3 ; print(f"Pay {bill}")
    else : print(f"Pay {bill}")

else : print("Not today!")
print("*" * 30)
print("   WELCOME TO TIP CALCULATOR  ")
print("*" * 30)


total_bill = float(input("What is the total bill : "))
number_of_people=int(input("How many people are splitting the bill : "))
percent = float(input("What tip percentage do you want to apply :  "))

tip_calc = total_bill*(percent/100)
bill_calc = total_bill/number_of_people
total_pay= tip_calc/number_of_people+bill_calc 

print('*'*30)
print(f"Total Tip : {tip_calc}")
print(f"Per person needs to pay {total_pay:.2f}")

print("*"*30)
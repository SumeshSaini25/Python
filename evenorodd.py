num = int(input("Enter a number : "))
k = {0 : "Even",1 : "Odd"}
print(f"The num {num} is {k[num % 2]}")
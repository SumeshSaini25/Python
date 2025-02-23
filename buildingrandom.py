"""
Documentation:
Main Goal is to make pseudo random numbers without using random modules in anyway to make sure we get a basic
understanding of how random module functions,because as we know genrating actual random numbers is not possible.
Approach : Using time module to use time.time() which is counting each seconds with microseconds since 1/01/1970.
In this we are using LGN and XORSHIFT algoritms as well.
"""
import time
main_seed=int(time.time()*100000)%1000003
seed = main_seed
a = ((int(time.time() * 1000) % 99991) * 7 + 13) % 99991 
c = ((int(time.time()) % 31337) * 3 + 17) % 31337 
m = ((int(time.time() * 1000) % 104729) * 5 + 19) % 104729
count = []
num = int(input("How many digit random number do you want : "))
numnum = int(input("How many numbers do you need : "))
for i in range(numnum):

    lower_bound = 10**(num-1)
    upper_bound=10**num-1
    shiftamount= int(time.time()*1000%31)+1
    formula = ((seed*a+c)^(seed>>shiftamount))%m
    seed = formula
    random_number = lower_bound+(formula%(upper_bound-lower_bound+1))
    count.append(random_number)
print(f"Here are {numnum}, {num} digit numbers",*count)




    


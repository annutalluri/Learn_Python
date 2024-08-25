print("welcome to pizza shop")
pizzasize = input("enter the pizza size s / m / l")
topping = input("do you need a topping yes/no")
extracheese = input("do you need a cheese yes/no")


bill = 0

if pizzasize == "s":
    bill += 15
elif pizzasize == "m":
    bill +=20

else:
    bill +=25

if topping == "yes":
    if pizzasize == "s":
        bill += 2
    else:
        bill += 3
if extracheese == "yes":
    bill += 1
else:
    bill += 0

print(f"your final bill is ${bill}")



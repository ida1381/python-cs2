import random
a,b=1,100

number=random.randint(a,b)
print(number)
javab = input("hads:")
while javab !="d":
    if javab == "b":
        a= number
        number = random.randint(a,b)
        print(number)
    elif javab == "k":
        b = number
        number = random.randint(a,b)
        print(number)
    
    javab = input("hads: ")

    
print("hads dorost bod")    

import random
a,b=1,100

number=random.randint(a,b)
hadsma=int(input("number"))

while number!= hadsma:
    if hadsma > number:
        #a=number
        #hadsma=int(input("number"))
        print("ye adad kochik tar hads bezan" )

    elif hadsma < number:
        #b=number
        #hadsma=int(input("number"))
        print("yek adad bozorgtar hads bezan")
        
    elif hadsma==number:
        print("good job")


    hadsma= int(input("number:"))

print("corect")

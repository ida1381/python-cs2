name=input("name:")
name= name.lower()
z ="aeiou"
result=""
for i in name:
    j = i in z
    if j == True:
        pass
    else:
        result+=i

natije= ""
for i in result:
    x = "."+i
    natije+=x

print(natije)

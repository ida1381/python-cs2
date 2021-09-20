number1=input("number1:")
number2=input("number2:")
number3=input("number3:")
number4=input("number4:")
number5=input("number5:")
list1=[ number1 , number2  , number3  , number4   , number5 ]
list1.sort(reverse=True)
#list1.reverse()
print("number1:" , list1[0] , "\tnumber2:" , list1[1] , "\tnumber3:" , list1[2] , "\tnumber4:" , list1[3] , "\tnumber5:" , list1[4])
jam=int( number1) +int( number2) +int( number3) +int( number4) +int( number5)
average=jam/5
print("average:" , average )

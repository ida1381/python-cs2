name1=input("name1:")
name2=input("name2:")
name3=input("name3:")
name4=input("name4:")
name5=input("name5:")
list1=[ name1 , name2   , name3   , name4   , name5 ]
list1.sort()
print("name1:" , list1[0] , "\nname2:" , list1[1] , "\nname3:" , list1[2] , "\nname4:" , list1[3] , "\nname5:" , list1[4])
q=list1[0] == list1[1]
print("is name1 and name2 the same?" , q)




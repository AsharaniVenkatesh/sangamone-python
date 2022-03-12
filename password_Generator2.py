def passgen1():
    
    import random
    list1=["a","b","c","d","e","f","g","h","i"]
    list2=["A","B","C","D","E","F","G","H","I"]
    list3=["1","2","3","4","5","6","7","8","9"]
    list4=list1+list2+list3
    pwd1=""
    rand1=random.randint(0,8)
    rand2=random.randint(0,8)
    rand3=random.randint(0,8)
    rand4=random.randint(0,26)
    rand5=random.randint(0,26)
    rand6=random.randint(0,26)
    rand7=random.randint(0,26)
    rand8=random.randint(0,26)

    pwd1=pwd1+list1[rand1]+list2[rand2]+list3[rand3]+list4[rand4]+list4[rand5]+list4[rand6]+list4[rand7]+list4[rand8]
    print(pwd1)
for i in range(0,10,1):
    passgen1()

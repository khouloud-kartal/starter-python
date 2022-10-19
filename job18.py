def myFunction( *numbers):
    list=[] 
    for i in numbers:
        if type(i) is int:
            list.append(i)
        else:
            print("uniquement des nombres.")
            return
    myList=[] 
    while list:
        a = list[0]  
        for y in list: 
            if y < a:
                a = y
        myList.append(a) 
        list.remove(a)
            
   
    print(myList)

myFunction(1,0,6,3,8,2)
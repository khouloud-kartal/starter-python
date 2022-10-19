def myFunction(*numbers):

    mylist = []    
    for i in numbers:
        mylist.append(i)
    print (sorted(mylist))


myFunction(0,10, 5, 1, 8, 2)
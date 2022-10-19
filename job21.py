
mylist = [1,6,0,4,8]

def mySort(*numbers):
   
    for i in numbers:
        mylist.append(i)
    return sorted(mylist)

def myDisplay (mylist):
    return (mylist)


print(myDisplay(mySort()))
# array based implementation in lists...
# array implementation insertion 

# def create():
   
# print(create())



def insertion():
    list_name = []
    print("Enter the number of elements to be added to list ")
    n = int(input("len of list"))

    for i in range(0,n):
        k = int(input("values:::"))
        list_name.append(k)
        i = i + 1
        
    print(list_name)

    # array creation complete
    # insertion start

    n = len(list_name)
    data = int(input("enter the value to be changed"))
    pos = int(input("enter the position"))
    if(pos==n):
        print("Array overflow")
        for i in range(n-1,pos-1):
            i = i-1
            list_name[i+1]=list_name[i]
        list_name[pos-1]=data
        
        n=n+1
        print(list_name)
    print(list_name)
print(insertion())
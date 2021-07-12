# array based implementation in lists...
# for eaiser access

def create():
    list_name = []
    print("Enter the number of elements to be added to list ")
    n = int(input("Values"))

    for i in range(0,n):
        k = int(input("values:::"))
        list_name.append(k)
        i = i + 1
        
    print(list_name)
print(create())

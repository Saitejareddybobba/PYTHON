# 3 arrays
# 1 original
# 2 temporaty
# 3 new

a = int(input("Enter the size of array"))
x = []
i = 0
for i in range(0,a):
    b = int(input(""))
    x.append(b)

print(x)

def Array_rotate(x,a,d):
    #x = array
    d = int(input("Enter the rotation value"))
    temp = x[0]
    print("the temporary array is",temp)
    for i in range(d):
        left_rotate(x,a)

def left_rotate(x,a):
    temp = x[0]
    for i in range(a-1):
        x[i] = x[i + 1]
    x[a-1] = temp
    
def printArray(x, size):
    for i in range(size):
        print ( x[i], end =" ")
 

Array_rotate(x, 2, )               # function calling
printArray(x, 7)

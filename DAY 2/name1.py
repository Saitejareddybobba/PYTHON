def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)
 
# Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp
         
 
# utility function to print an array */
def printArray(arr, lamo):
    for i in range(lamo):
        print ("% d"% arr[i], end =" ")
 
  
# Driver program to test above functions */
arr = []
size = int(input("size"))
for i in range(size):
        k = int(input(""))
        arr.append(k)

leftRotate(arr, d = int(input("enter an value")), n = size)
printArray(arr, lamo=size)
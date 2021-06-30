# find the largest number in a array

def Mamimum(arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]

    return max

arr = [1,2,3,4,5,6,7,8,9]    
n = len(arr)
k = Mamimum(arr,n)
print("the answer is ",k)

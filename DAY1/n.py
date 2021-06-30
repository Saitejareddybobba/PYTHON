#sum of squares of a number

def Square(num):
    sm = 0
    for i in range(1,num+1):
        sm = sm + (i * i)
        
    
    return sm

num = int(input("Enter an number::"))

print(Square(num))



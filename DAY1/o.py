# Cube sum

def Cube_sum(num):
    sm = 0
    for i in range(1,num+1):
        sm = sm + (i * i * i)
    return sm

num = int(input("Enter a number::"))

print(Cube_sum(num))

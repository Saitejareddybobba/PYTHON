# factorial of a number

a = int(input("Enter a number:"))
#fact = a
#sum = 0.0
#for i in range(0,a+1):     # i would have used a while loop
#    fact = fact * a
#    sum = sum + fact       // does not needed
#    i+=1                   // we need to decrement
#print(fact)   

if(a<0):
    print("Wrong input")
elif(a==0 or a==1):
    print("The factorial is 1")
else:
    fact = 1
    while(a > 1):
        fact = fact * a
        a = a - 1
print(fact)


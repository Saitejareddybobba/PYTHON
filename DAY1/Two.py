# code for hackerrank python (2)
# using multiple looping techniques.
k = int(input("Enter an Number::"))
if(k % 2 == 1) :
    print("Weird")
else:
    for k in range(2,5):
        print("Not Weird")
        break

    for k in range(6,20):
        print("Weird")
        break

    if(k > 20 ):
        print("Not Weird")



# same problem 
# only useing if-else statements

k= int(input("Enter an integer::"))
if (k>0):
    if(k%2 == 1):
        print("Weird")
    
    else:
        if k in range(2,5):
            print("Not Weird")

        elif k in range(6,20):
            print("Weird")

        elif( k > 20):
             print("Not Weird")
             
              

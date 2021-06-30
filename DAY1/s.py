# python program to interchange first and last elements



def list_xchange(list_name):
        size = len(list_name)
        
        n = int(input("Enter an value::"))
        m = int(input("Enter an value::"))
        
        temp = list_name[n]
        list_name[n] = list_name[m]
        list_name[m] = temp

        return list_name
       

list_na = [1,2,3,4,5,6,7,8,9]

print(list_na)
print(list_xchange(list_na))

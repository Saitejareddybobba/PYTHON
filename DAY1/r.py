# python program to interchange first and last elements



def list_xchange(list_name):
        size = len(list_name)

        temp = list_name[0]
        list_name[0] = list_name[size - 1]
        list_name[size - 1] = temp

        return list_name

list_na = [1,2,3,4,5,6,7,8,9]

print(list_na)
print(list_xchange(list_na))

# no of elemnets in list

def List_elemnts(list_name):
    sum = 0
    for i in list_name:
        print(i)
        sum = sum + i

    return sum   

list_na = [1,2,3,4,5,6,7,8,9]

print(List_elemnts(list_na))
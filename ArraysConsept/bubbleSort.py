


my_array =  [30,12,60,13]

n = len(my_array)
for i in range(n-1):
    for j in range(n - i -1):
        temp = my_array[j]
        if my_array[j] > my_array[j + 1]:
            my_array[j] = my_array[j + 1]
            my_array[j + 1] = temp
            # my_array[j], my_array[j + 1]  = my_array[j + 1], my_array[j]
            

print("sorted array", my_array)











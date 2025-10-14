my_array = [3,23,14,6]
n = len(my_array)


min_value = my_array[0]
for i in range(0,n):
  if(my_array[i] < min_value):
    min_value = my_array[i]

print(min_value)

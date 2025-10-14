my_array =  [3,12,6,13]
n = len(my_array)
max_value = my_array[0]

for i in range(0, n):
  if(max_value < my_array[i]):
    max_value = my_array[i]

print(max_value)

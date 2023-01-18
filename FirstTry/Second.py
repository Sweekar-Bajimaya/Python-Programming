num_string = '15'
num_integer = 25
print('Data type of num_string before type casting: ',type(num_string))

num_string = int(num_integer)
print('Data type of num_string after type casting: ',type(num_string))

num_sum = num_string + num_integer

print("sum: ", num_sum)
print("data type of num_sum: ", type(num_sum))

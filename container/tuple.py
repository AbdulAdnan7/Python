#containers

a_tuple = (1, 2, 3, 'a string')
print(a_tuple) # cannot append bcz it is immutable
a_list = [1,2,3, 'a string']
a_list = [2,3,45]
a_list.append("Another word")
print(a_list)
a_set = {1, 2,  3, 4, 4, 4} # will not print 4 more than one time
print(a_set)
print(set(a_list))

b_list = [1,3,4,2,4,5,7,54] # using set() will print it in ascending order
print(set(b_list))

a_dictionary = { "key" : "Value", 123: [1,3,4,3,2,3] }
print(a_dictionary)
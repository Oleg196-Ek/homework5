 # immutable_var = 1, 2, True, 'String', [4, 5, 7], False
 # print(immutable_var)
 # immutable_var[] = 500
 # print( immutable_var) # кортеджи неизменны.
# Это означает, что мы не можем добавить, удалить или изменить элементы кортежа после того,
# как определили его.
mutable_list = ['pen', 'pencil', 'line', 'pencil box']
print(mutable_list)
print(mutable_list [0])
mutable_list [0] = 'line'
print(mutable_list)
print(mutable_list [3])
mutable_list [3] = 'pen'
print(mutable_list)
name='Immutable_var :'
tuple_= (1, 2, 'a','b') # переменные в кортеже не изменяются
print(name, tuple_)
#tuple_[0]=100 # при таком вводе выдает ошибку
# print(tuple_[0])
name='Mutable_list :'
list = [1 , 2, "a", "b"]
print(name, list)
list.append('Modified')
print(name, list)
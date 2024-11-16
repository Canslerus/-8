# Словарь
my_dict = {'Den': 1990, 'Bob': 1991}
print(my_dict)
print(my_dict.get('Den'))
print(my_dict.get('Lola'))
my_dict['Lola']=2000 # первый способ добавить
my_dict.update({'Don':1980}) # второй способ добавить
print(my_dict.pop('Bob'))
print(my_dict)
# Множества
my_set = {True, 'b', 'a', 7, 2, 4, 4, 'a', True, 7}
print(my_set)
my_set.add (5)
my_set.add('hh')
my_set.discard(4)
print(my_set)
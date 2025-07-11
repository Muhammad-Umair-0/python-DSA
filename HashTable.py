def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    
    return sum_of_chars % 10

print("'Umair' has hash code : ", hash_function('Umair'))

my_list = [None, None, None, None, None, None, None, None, None, None]

def add(name):
    index = hash_function(name)
    my_list[index] = name


add('Bob')
add('Umair')
add('Ali')
add('Hamza')
print(my_list)

# using the hash table to find the name index
def contains(name):
    index = hash_function(name)
    return my_list[index] == name
print("'Umair' is in the hash table ", contains('Umair'))


my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]
# Handling the chaining 
# Rewrite the add Function 
def add(name):
    index = hash_function(name)
    my_list[index].append(name)

add('Umair')
add('Umair')
add('Ali')
print(my_list)

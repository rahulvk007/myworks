#PAT 3 AND 4 PORTIONS : LIST , TUPLE, DICTIONARY , SETS

#dict.clear() removes all elements of a dictionary. It returns None

d = {'1': 'one', '2': 'two', '3': 'three'}
'''
print(d)
d.clear()
print(d)
'''
#dict.copy() creates a copy of the dictionary
'''
When the copy() method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary.
When the = operator is used, a new reference to the original dictionary is created.
'''

#dict.fromkeys(sequence, value)
'''
a = ['a', 'e', 'i', 'o', 'u']
k = dict.fromkeys(a)
print(k)
'''
'''
get(key, value) method returns:

the value for the specified key if key is in the dictionary.
None if the key is not found and value is not specified.
value if the key is not found and value is specified.
'''
#print(d.get('1'))

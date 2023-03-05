# Declaration of dictionary
a = dict()
# or you can just put {}
b = {}
a = {'key1' : 'value1', 'key2': ' value2'}
a['key3'] = 'value3'

try:
    print(a['key4'])
except KeyError:
    print('Doesn\' exist')

if 'key4' in a:
    print("key4 exists in dict a")
else:
    print("Doesn't exist in dict a")

for k,v in a.items():
    print(k, v)





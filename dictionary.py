
print('Dictionary \n')
dic1={'Name:':'Pravii','Age:':17,'class:':'Plus Two'}
print('print name \n')
print("dic1['Name']:",dic1['Name:'])
print('print age \n')
print("dic1['Age']:",dic1['Age:'])

print('print dic1 \n')
print(dic1)

print('only print keys \n')
print(dic1.keys())

print('only print values \n')
print(dic1.values())

print('To get the type \n')
type(dic1)

print('ANOTHER DICTIONARY: \n')

dict={}
dict['one']="This is one"
dict[2]="This is two"
print("dict['one']:",dict['one'])

print("dict[2]:",dict[2])

print(dict.keys())
print(dict.values())

print('Length of dic \n')
print(len(dict))

print('representation of string \n')
print(str(dict))

print('type \n')
print(type(dict))

"""print('To clear \n')
print(clear(dict))"""
print('copy dictionary: \n')
dict1=dict.copy()
print(dict1)


print('items \n')
print(dict.items())

print('UPdate \n')
dict2={'weight:':18}
dict.update(dict2)

print(dict)
print()


list1=['abc',45,6,70,85,21,'manu']
print(list1)

print('To APPEND \n')
list1.append(70)
print(list1)

print('To COUNT \n')
print(list1.count(45))
print(list1)

print('To REMOVE \n')

print(list1.remove(6))
print(list1)

print('To GET INDEX \n')
print(list1.index(21))
print(list1)

print('To GET INDEX \n')
print(list1.index('abc'))
print(list1)

print('To EXTEND LIST \n')
list2=[18,'cs']
list1.extend(list2)
print(list1)

print('To REVGERSE\n')
list1.reverse()
print(list1)


print('insert \n')
list1.insert(3,1000)
print(list1)

print('sort \n')
list1.sort()
print(list1)

print('pop \n')
list1.pop(2)
print(list1)
print('pop 1 \n')
list1.pop(1)
print(list1)

print('pop  0\n')
list1.pop(0)
print(list1)

print('pop -1 \n')
list1.pop(-1)
print(list1)

print('pop -2 \n')
list1.pop(-2)
print(list1)

print('copy() \n')

list2=list1.copy()
print(list2)

print('clear \n')
list.clear()



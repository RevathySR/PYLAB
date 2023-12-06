
print('Specifies the range only \n')
print(range(10))

print(' \n Specifies the range with list \n')
print(list(range(10)))
print(' \n Specifies the range with starting and ending value \n')


print(list(range(2,8)))

print(' \n Specifies the range with start with 2 and end with 20 incrementing 3\n')

print(list(range(2,20,3)))


print('\n range function in for loop ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n')

gen=['pop','rock','jazz']
for i in range(len(gen)):
    print("I LIKE ",gen[i])
    

print('\n num range..........................................  \n ')

for num in range(2,10,2):
    print("number:",num)

print('\n print num range..........................................  \n ')

for i in range(1,11):
 print(i)

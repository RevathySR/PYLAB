print(' Normal List ....................................... \n ')




list1=[2,4,-6,-8,9,7]
list2=[]
for i in list1:
    if i>0:
        list2.append(i)
print(f" \n Positive list={list2} \n")


print('\n  List Comprehension....................................... \n ')
list1=[2,4,-6,-8,9,7] #code shorthanded
list2=[i for i in list1 if(i>0)];
print(f"positive list ={list2}")

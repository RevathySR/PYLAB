n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print("1.Addition\n 2.Substraction\n 3.Multiplication\n 4.division\n")
ch= int(input("Enter your choice:"))
if ch ==1:
 sum=n1+n2
 print("sum of two numbers:",sum)
elif ch ==2:
 sum=n1-n2
 print("Difference of two numbers:",sum)
elif ch ==3:
 sum=n1*n2
 print("Multiple of two numbers:",sum)
elif ch ==4:
 sum=n1/n2
 print("quotient of two numbers:",sum)
else:
    print("Enter correct choice!!!")

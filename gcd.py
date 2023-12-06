
print("FIND GCD OF 2 NUMBERS..........................................")
num1=int(input("Enter first num1: "));
num2=int(input("Enter second num2 : "));
if num1>num2:
    min=num1
else:
    min=num2
gcd=1
for i in range(1,min+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(f"The GCD on {num1} and {num2} is {gcd}")
    

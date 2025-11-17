a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
s = (a+b+c)/2
area = pow((s*(s-a)*(s-b)*(s-c)), 1/2)
print(area)
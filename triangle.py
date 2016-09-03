s=raw_input("Enter the sides of triangle like(x,y,z) : ")
sides=map(int,s.split(","))
print sides
def isTriangle(sides):
        small,medium,big=sorted(sides)
        return small+medium>=big and all(s>0 for s in (sides))
print isTriangle(sides) 
a,b,c=sides
if isTriangle(sides)==True:
	if a==b==c:
		print "Equilateral Triangle !"
	elif a!=b!=c:
		print "Scalene Traingle !"
	else:
		print "Isosceles Triangle !"
else:
	print("This is not a Triangle according to 'Triangle Inequality Theorem' ! ")
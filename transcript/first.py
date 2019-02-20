# list_c=[6,7,8]
# list_b=[3,4,5]
# list_a=[1,2]
# list_b.append(list_c)
# list_a.append(list_b)
# print (list_a)
# print (list_a[-1][-1])
# if (7 in list_a[-1][-1]):
# 	print ("Exist")

# list_b=[3,4,5]
# list_a=[1,2]
# list_a.append(list_b[:])
# print (list_a)
# list_b[-1]=99
# print (list_b)
# print (list_a)

# a=4
# list_a=[a,4,5]
# print (list_a)
# print (a)
# a=5
# print (list_a)
# print (a)
# del list_a[0]
# del a
# name      address #100     value  4    count 0
# name       address #101     value  4    count 1
# name       address #102     value  5    count 1
# name list_a  address #250    value [#101,#102]
# name      address #104     value  5    count 0

# list_a=[1,2,3,4]
# list_b=[5,6,7,8]
# # Shallow Copy Methods
# list_a.append(list(list_b))  # Only when you are sure about list
# list_a.append(list_b.copy()) # Preferred when dynamic contents possibilities
# list_a.append(list_b[:])  # Not Preferred
# list_b[0]=99
# print (list_a)
# print (list_b)

# import copy
# list_a.append(copy.copy(list_b))

# # Nested Data Structure
# import copy   # Available in Python 3.x and 2.x
# list_a=[1,2]
# list_b=[3,4]
# list_c=[5,6]
# list_b.append(list_c)
# list_a.append(copy.deepcopy(list_b))  # Recursive Copy
# print (list_a)
# list_b[0]=99
# print (list_a)
# list_c[0]=100
# print (list_b)
# print ("For A",list_a)

# list_a=[1,2]
# list_b=[3,4]
# list_a.extend(list_b)

# list_a=[0,1,2,3,4,5,6]
# list_a.insert(0,"Hello")
# print (list_a)
# list_a.insert(2,"World")
# print (list_a)
# print (len(list_a))
# list_a.insert(-1,"OKAY")
# # list_a.remove("Hello")  # remove by value
# # del list_a[0]
# print (list_a)
# print (list_a.index("Hello"))
# list_a.clear()
# print (list_a)

# list_a.insert(len(list_a),"Hello")

# tuple_a=(1,2,3,4,)
# for x in tuple_a:
# 	print (x)
# for x,y in enumerate(tuple_a):
# 	print (x,y)

# x=4
# y=6
# z=45
# print (x,y,z)
# x,y,z=y,z,x
# print (x,y,z)

# print (x,y,z)
# x=y,z,x
# print (x)
# print (type(x))
# for h in x:
# 	print (h)
# a="Hello World"
# print (list(enumerate(a)))

# list_a=[1,2,3,4]
# for x in enumerate(list_a):
# 	print (x)
# 	print (type(x))


# def printme():
# 	print ("Hello World")
# 	print ("Okay")
# 	return "GREAT","OKAY",7 # multiple values can be sent back

# # one to one assignment (Tuple Concept)
# a,b,c=printme()
# print (a,b,c)

# # Default Return valueof a function is None
# def printme():
# 	print ("Hello World")
# a=printme()
# print (a)

# def printme(a,b):
# 	print (a,b)
# 	return a+b

# print (printme(2,3))

def F1(a):
	a()
	print ("F1",a)

def F2():
	print ("F2")

def F3():
	print ("F3")
	return F2

# F1(F2)

# g=F3()
# print (g)
# g()

F3()()z




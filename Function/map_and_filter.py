#map function apply same function to all element
list1=[1,2,3,4,5,6]
result=map(lambda x:x*2,list1)
print(list(result))

#filter function return True element
number=[2,35,6,7,8,9]
final=filter(lambda x:x%2==0,number)
print(list(final))
list=[1,2,3,4,5,6,7,8,9,10]
first,*middle,last=list

print(first)
print(middle)
print(last)

Total=0
count=0
for i in middle:
    Total+=i
    count+=1

print(Total/count)
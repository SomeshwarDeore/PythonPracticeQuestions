tuple=1,2,3,4,5,6,7,8
first,*middle,last=tuple

print(first)
print(middle)
print(last)

for i in middle:
    if i%2==0:
        print(i)
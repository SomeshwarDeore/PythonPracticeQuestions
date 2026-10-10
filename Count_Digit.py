text=input("Enter any text")
count=0

for i in text:
    if(i.isdigit()==True):
        count+=1
        
print("Total number of integer in your text is :",count)        
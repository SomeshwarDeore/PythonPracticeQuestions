text=input("Enter any text :")
string=""

for i in text:
    if(((i.isalpha()==True) or (i.isdigit()==True)) or(i==" ")):
        string+=i
        
print(string)
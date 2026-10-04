# use recursive function
def fact(n):
    if n==1 or n==0: # Base case
        return 1
    
    else:
        return n*fact(n-1)
print(f"Factorial is :{fact(5)}")      
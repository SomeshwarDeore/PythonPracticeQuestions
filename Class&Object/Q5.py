class ComplexNumber: 
    # Fixed: Changed _init_ to __init__
    def __init__(self, real, imaginary): 
        self.real = real 
        self.imaginary = imaginary 
        
    def __add__(self, other): 
        real = self.real + other.real 
        imaginary = self.imaginary + other.imaginary 
        return ComplexNumber(real, imaginary) 
        
    def display(self): 
        print(self.real, "+", self.imaginary, "i") 

# Objects 
c1 = ComplexNumber(5, 3) 
c2 = ComplexNumber(2, 4) 

# Addition 
c3 = c1 + c2 
c3.display()  # Output: 7 + 7 i

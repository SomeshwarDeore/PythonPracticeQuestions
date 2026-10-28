def lambda_square(square,number):
    return square(number)

square=lambda x:x**2

print(lambda_square(square,5))
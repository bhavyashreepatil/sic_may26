#Factorial
def find_factorial(number):
    if number==1 or number==0:
        return 1
    temp_number= number*find_factorial(number-1)
    return temp_number

    


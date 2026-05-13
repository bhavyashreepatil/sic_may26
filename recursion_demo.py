import sys
import recursion as rc
input_number=int(sys.argv[1])
factorial_number=rc.find_factorial(input_number)
print(f"Factorial of {input_number}is {factorial_number}")
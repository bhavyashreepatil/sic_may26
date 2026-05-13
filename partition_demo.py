import sys
import partition as pt

numbers=[int(value) for value in sys.argv[1:]]
print("Numbers before partition \n :",numbers)
pt.partition_array(numbers)
print("Numbers after partition:\n")
for i in range(len(numbers)):
    print(numbers[i],end=" ")    
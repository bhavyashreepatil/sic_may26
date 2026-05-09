import insertionsort as ins
import sys
numbers=[]
for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))
print("Numbers vefore sorting:\n ",numbers)
ins.insertion_sort(numbers)
print("Numbers after sorting:\n ")    
for i in range(len(numbers)):
    print('%-4d'%(numbers[i]),end="")


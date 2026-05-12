import sys
import selectionsort as ss
numbers=[]
for i in range(1,len(sys.argv)):
    numbers.append(sys.argv[i])
print("Numbers before sorting \n :",numbers)
ss.selection_sort(numbers)
for i in range(len(numbers)):
    print(numbers[i],end=" ")    
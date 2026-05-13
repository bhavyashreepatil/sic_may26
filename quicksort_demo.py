import sys
import quicksort as qs

numbers=[int(value) for value in sys.argv[1:]]
print("Numbers before sort \n :",numbers)
qs.quick_sort(numbers,0,len(numbers)-1)
print("Numbers after sort :\n")
for i in range(len(numbers)):
    print(numbers[i],end=" ")    
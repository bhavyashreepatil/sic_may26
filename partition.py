def partition_array(numbers,low,high):
    pivot=numbers[high] #asign last element of partitioned array as reference elemnet
    i=low   #to access each elemnet of the list
    j=low    #to find the index of pivot element

    for i in range(low,high):
        if numbers[i]<pivot:
            numbers[i],numbers[j]=numbers[j],numbers[i]
            j+=1
    numbers[high],numbers[j]= numbers[j],numbers[high]
    #return numbers     
    return j
    




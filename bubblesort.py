input_list=[]
def bubbleSort(input_list):
    
    for i in range(0,len(input_list)-1):
        for j in range(0,len(input_list)-1-i):
            if input_list[j]>input_list[j+1]:
                input_list[j],input_list[j+1]=input_list[j+1], input_list[j]
    return input_list

def OptimisedBubbleSort(input_list):


                


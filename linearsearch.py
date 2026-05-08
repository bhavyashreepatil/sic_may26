'''
LINEAR SEARCH
read size of list from user
read the search elememt from the userfrom user
ask teh function sequentailly search
return first occurence of element or -1 is dont exit
'''
def LinearSearch(search_element,elements):
    for i in range(len(elements)):
        if elements[i]==search_element:
            return i
    return -1    
input_size=int(input("Enter size of list: "))
elements=[]
print(f"enter the {input_size} elements of the list:  ")
for i in range(input_size):
    element=float(input())
    elements.append(element)
print("User given elements are \n",elements)
search_element=float(input("Enter element to search: "))    
search_index=LinearSearch(search_element,elements)
if search_element==-1:
    print(f"The search element {search_element} was not found in the yyyy")
else:
    print(f"The search element {search_element} was found at position{i}")

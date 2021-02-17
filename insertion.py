#----------------------------------------------------------------------#
#    Illustration of Insertion sort in Python                          #
#----------------------------------------------------------------------#
# Function to do insertion sort
def insertion_sort(sort_list):
    for i in range(1, len(sort_list)): # Traverse through 1 to len(list)
        key = sort_list[i]
# Move elements of list[0..i-1], that are
# greater than key, to one position ahead
# of their current position
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    print('\nThe sorted salary list is: \t', sort_list)
    print("Highest salary is:", max(sort_list))
    print("Lowest salary is:", min(sort_list)) 
    print('\n')
lst = []
size = int(input("\nEnter the number of employees: \t"))
for i in range(size):
    elements = int(input("Enter the employee salary: \t"))
    lst.append(elements)
insertion_sort(lst)


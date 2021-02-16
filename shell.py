# Shell sort in python


def shellSort(array, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


data = [] 
  
# number of elemetns as input
print('                          MOUNT CARMEL COLLEGE                           ')
print('=========================================================================')
print('                      EXAMINATION SEATING ARRANGEMENT                    ')
print('=========================================================================')
d = int(input("ENTER THE NUMBER OF STUDENTS: "))
print('=========================================================================')
print('ENTER ' + str(d) + ' STUDENTS REGISTER NUMBER : ')
  
# iterating till the range 
for i in range(0, d): 
    ele = int(input()) 
  
    data.append(ele) # adding the element 

size = len(data)
shellSort(data, size)
print('=========================================================================')
print('**************SORTING STUDENTS ACCORDING TO REGISTER NUMBER**************')
print('=========================================================================')
print(data)
print('=========================================================================')
print('******************************THANK YOU**********************************')
print('=========================================================================')

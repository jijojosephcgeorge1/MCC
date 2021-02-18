#Program to store the loan amount taken by various customers of XYZ bank in the month of January.
# sort the loan amount taken in order to help the bank
#to analyze and keep track of the smaller and larger amount of loan given by them.

# to perform sort
def insertion_sort(arr):
   for i in range(1, len(arr)):
      temp = arr[i]
      pos = binary_search(arr, temp, 0, i) + 1
      for k in range(i, pos, -1):
         arr[k] = arr[k - 1]
      arr[pos] = temp
#performing binary search
def binary_search(arr, key, start, end):
    # we need to distinugish whether we should insert 
    # before or after the left boundary. 
    # imagine [0] is the last step of the binary search 
    # and we need to decide where to insert -1 
   #key
   if end - start <= 1:
      if key < arr[start]:
         return start - 1
      else:
         return start
   mid = (start + end)//2
   if arr[mid] < key:
      return binary_search(arr, key, mid, end)
   elif arr[mid] > key:
      return binary_search(arr, key, start, mid)
   else:
      return mid
# main module
arr = []

print("\n Program to store the loan amount taken by various customers of XYZ bank in the month of january in a sorted manner")
n=int(input("\n Enter the number of customers who have taken loan in the month of january: "))
print(n)
print("Enter the loan amount taken by the customers")
for i in range(n):
   print("loan taken by customer ",i+1)
   ele = int(input())
   arr.append(ele) # adding the element
print("Loan amount taken by cutomers before sorting")
print(arr)
insertion_sort(arr)# calling the insertion sort function
print("The range of loan amount taken in the month of january is printed in a sorted manner")
print("to analyse & keep track of the smaller and larger amount of loan taken :")
print(arr)

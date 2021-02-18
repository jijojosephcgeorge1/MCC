def quicksort(Mylist):
    n=len(Mylist)
    Rec_quicksort(Mylist, 0, n-1)
 
def Rec_quicksort(Mylist, first, last):
    if first<last:
        pos=position(Mylist, first, last)
        Rec_quicksort(Mylist, first, pos-1)
        Rec_quicksort(Mylist, pos+1, last)
 
def position(Mylist, first, last):
    pivot=Mylist[first]
    i=first
    j=last
 
    while i<j:
        while i<=j and Mylist[i]<=pivot:
            i=i+1
        while pivot<Mylist[j]:
            j=j-1
        if i<j:
            temp=Mylist[i]
            Mylist[i]=Mylist[j]
            Mylist[j]=temp
 
    temp=Mylist[first]
    Mylist[first]=Mylist[j]
    Mylist[j]=temp
    return j
 
Mylist=[ 50, 30, 10, 90, 80, 20, 40, 60 ]
print("Given list:",Mylist)
 
quicksort(Mylist)
print("After sorting list is:",Mylist)

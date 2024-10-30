import math

def  bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
    return arr



def selection_sort (arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr [j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr



def insertion_sort(arr):
    for i in range(1,len(arr)):
        next=arr[i]
        prev=i-1
        while prev >= 0 and next < arr[prev]:
            arr[prev+1]=arr[prev]
            arr[prev]='*'
            prev-=1
        arr[prev+1]=next
    return arr



def bucket_sort (arr):
    number_of_buckets=round(math.sqrt(len(arr)))
    max_value=max(arr)
    temp_array=[]
    for _ in range(number_of_buckets):
        temp_array.append([])
    for i in arr:
        index_b=math.ceil(i*number_of_buckets/max_value)
        temp_array[index_b-1].append(i)
    for i in range(number_of_buckets):
        temp_array[i]=insertion_sort(temp_array[i])
    k=0
    for i in range(number_of_buckets):
        for j in range(len(temp_array[i])):
            arr[k]=temp_array[i][j]
            k+=1
    return arr



def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m 

    L= [0] * n1
    R= [0] * n2

    for i in range(len(L)):
        L[i] = arr[l+i]

    for j in range(len(R)):
        R[j] = arr[m+1+j]
    i=0
    j=0
    k=l

    while i <  n1 and j <  n2:
        if L[i] <= R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i < n1:
        arr[k]=L[i]
        i+=1
        k+=1

    while j < n2:
        arr[k]=R[j]
        j+=1
        k+=1

    return True

def merge_sort(arr):
    def _mergeSort(arr,l,r):
        if l < r:
            m = l + (r - l) // 2
            _mergeSort(arr,l,m)
            _mergeSort(arr,m+1,r)
            merge(arr,l,m,r)
        return arr
    return _mergeSort(arr,0,len(arr)-1)



def pivot (arr,pivotIndex,endIndex):
    swap_index=pivotIndex
    for i in range(pivotIndex+1,endIndex+1):
        if arr[pivotIndex] > arr[i]:
            swap_index+=1
            arr[swap_index],arr[i]=arr[i],arr[swap_index]
    arr[pivotIndex],arr[swap_index]=arr[swap_index],arr[pivotIndex]
    return swap_index

def quick_sort (arr):
    def _quicSort (arr,left,right):
        if left < right:
            pivot_index=pivot(arr,left,right)
            _quicSort(arr,left,pivot_index-1)
            _quicSort(arr,pivot_index+1,right)
        return arr
    return _quicSort(arr,0,len(arr)-1)



def heapify(arr, length, rootIndex):
    biggest = rootIndex
    left = 2 * rootIndex + 1
    right = 2 * rootIndex + 2
    
    if left < length and arr[left] > arr[biggest]:
        biggest = left

    if right < length and arr[right] > arr[biggest]:
        biggest = right
    
    if rootIndex != biggest:
        arr[rootIndex], arr[biggest] = arr[biggest], arr[rootIndex]
        heapify(arr, length, biggest)

def heap_sort(arr):
    n = len(arr)
    for i in range(int(n/2)-1, -1, -1):  
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)  
    return arr



array=[5,4,5,5,5,3]


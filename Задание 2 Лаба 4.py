## O(3n)
def LinearSearch(array, n, k):
    for j in range(0, n):
        if (array[j] == k):
            return j
    return -1
array = [1, 3, 5, 7, 9]
k = 7
n = len(array)
result = LinearSearch(array, n, k)

## O(nlogn)
unsorted_list = [2,4,5,32,6,255,5,42]
unsorted_list.sort()
print("Now it is sorted:", unsorted_list)

## O(n^2)
from random import randint
a=[]
for i in range (10):
    a.append (randint(1,100))
    print (a)
for i in range  (9):
 for j in range (9-i):
        if a[j]>a[j+1]:
            a[j], a[j+1]=a[j+1], a[j]
print (a)

## O(n!)
def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
    
if __name__ == '__main__':
    data = [1, 2, 3]
    heap_permutation(data, len(data))

## O(n^3)
list = [1, 2, 3]
n = len(list)
for i in range(0, n): 
   for j in range (0, n): 
       for g in range(0,n):
           print(g)

## O(3 log n)
def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

import math
from heapq import heappush, heappop

# -------------------insertion sort-------------------
# ""when we reach to an element we compare that element with others and find the correct place for that""
A = [3, 7, 4, 5, 0, -1, 9, 12, 10, 6, 3, 5, 6, -100]
for i in range(0, len(A)):
    item = A[i]
    k = i
    while k > 0 and A[k - 1] > item:
        A[k] = A[k - 1]
        k -= 1
    A[k] = item
print(A)
# -----------------------------------------------------

# ---------------------bubble sort---------------------
# ""from end compare each element with the last element if the last one was smaller we change them""
A = [3, 7, 4, 5, 0, -1, 9, 12, 10, 6, 3, 5, 6, -100]
n = len(A)
for j in range(n):
    bubble_found = False
    for i in range(n - 1, j, -1):
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            bubble_found = True
    if not bubble_found:
        break
print(A)
# ------------------------------------------------------

# -------------------counting sort----------------------
# ""count the number of every number has repeated""
A = [3, 7, 4, 5, 0, 9, 12, 10, 6, 3, 5, 6]
m = max(A)
Count = [0] * (m + 1)
for x in A:
    Count[x] += 1
Temp = []
for x in range(m + 1):
    Temp += [x] * Count[x]
print(Temp)
# -------------------------------------------------------

# -------------------selection sort----------------------
# ""chose the element and compare with next element and change that with the smallest one""
A = [3, 7, 4, 5, 0, 9, 12, 10, 6, 3, 5, 6]
num = len(A)
for i in range(num - 1):
    selection = i
    for j in range(i + 1, num):
        if A[j] < A[selection]:
            selection = j
    A[selection], A[i] = A[i], A[selection]
print(A)
# ---------------------------------------------------------

# --------------------merge sort---------------------------
# ""divide array to two array and continue this""
def mergeSort(array):
    if len(array) > 1:
        length = len(array)//2
        left = array[:length]
        right = array[length:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
array = [3, 7, 4, 5, 0, 9, 12, 10, 6, 3, 5, 6]
mergeSort(array)
print(array)
# -----------------------------------------------------------

# ----------------------bucket sort--------------------------
# ""change the array to ten array and use bubble sort for that""
def bubble_sort(A):
    n = len(A)
    for j in range(n):
        bubble_found = False
        for i in range(n - 1, j, -1):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
                bubble_found = True
        if not bubble_found:
            break
    return (A)

def bucket_sort(A):
    B = [[] for i in range(10)]
    for i in A:
        B[i // 10] += [i]
    print(B)
    A = []
    for i in range(10):
        A += bubble_sort(B[i])
    return A
array = [3, 7, 4, 5, 0, 9, 12, 10, 6, 3, 5, 6, 52, 48, 42, 51, 96, 95, 95, 91, 36, 37]
print(bucket_sort(array))
# ---------------------------------------------------------------

# ---------------------binary search-----------------------------
# ""found middle of an array and check that is this that we want or not""
def binary_search(array ,x):
    up = len(array) - 1
    down = 0
    while up >= down:
        mid = (up + down)//2
        if array[mid] == x:
            return "found at", mid + 1
        elif array[mid] < x:
            down = mid + 1
        else:
            up = mid - 1
    return "not found"
myArray = [1, 5, 9, 15, 21, 59, 100, 652, 666, 897]
print(binary_search(myArray, 666))
# ------------------------------------------------------------------

# ------------------------lower bound-------------------------------
# ""found the last smaller of one element""
def lower_bound(a, x):
    if a[0] >= x:
        return -1
    start = 0
    end = len(a)
    while end > start + 1:
        mid = start + end >> 1
        if a[mid] >= x:
            end = mid
        else:
            start = mid
    return start
# ------------------------------------------------------------------

# ------------------------upper bound-------------------------------
# ""found the next bigger of one element""
def upper_bound(a, x):
    if a[len(a)-1] <= x:
        return -1
    start = 0
    end = len(a)
    while end > start + 1:
        mid = start + end >> 1
        if a[mid] > x:
            end = mid
        else:
            start = mid
    return end
# ------------------------------------------------------------------

# ------------------------intro sort--------------------------------
arr = []


def heapsort():
    global arr
    h = []
    for value in arr:
        heappush(h, value)
    arr = []
    arr = arr + [heappop(h) for i in range(len(h))]


def InsertionSort(begin, end):
    left = begin
    right = end
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


def Partition(low, high):
    global arr
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def MedianOfThree(a, b, d):
    global arr
    A = arr[a]
    B = arr[b]
    C = arr[d]
    if A <= B and B <= C:
        return b
    if C <= B and B <= A:
        return b
    if B <= A and A <= C:
        return a
    if C <= A and A <= B:
        return a
    if B <= C and C <= A:
        return d
    if A <= C and C <= B:
        return d


def IntrosortUtil(begin, end, depthLimit):
    global arr
    size = end - begin
    if size < 16:
        InsertionSort(begin, end)
        return
    if depthLimit == 0:
        heapsort()
        return
    pivot = MedianOfThree(begin, begin + size // 2, end)
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])
    partitionPoint = Partition(begin, end)
    IntrosortUtil(begin, partitionPoint - 1, depthLimit - 1)
    IntrosortUtil(partitionPoint + 1, end, depthLimit - 1)


def Introsort(begin, end):
    depthLimit = 2 * math.floor(math.log2(end - begin))
    IntrosortUtil(begin, end, depthLimit)
# ------------------------------------------------------------------
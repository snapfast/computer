# quick sort

"""

Input:
7 4 8 9 2 5 1 6


Quick Sort algo:
1. Choose a pivot, partition the array at the pivot element. Generally, the middle element.
2. Start 2 pointers from start and end.
3. Swap the elements if the start is bigger than the end, and the end element is smaller than pivot.
4. Move one position, after swap, then check point 3 again.
5. Once completed, start from 1 to 4 in the left, then right partition. Until sorted. :)


Method design:

- partition(A, start, end)
this function will take input of the Array, start, end position.
And choose pivot element and will return the two partitions.

- quicksort(A, x, y)
this function will be used for recursion of the algo.
function is called with smaller set of start and end, for each iteration.
And will perform swap of elements in place.

"""

def partition(A, start, end):
    """
    create partition from the 
    """
    mid = ( start + end ) / 2
    return mid


def quicksort(A, first, last):
    pivot = partition(A, start, end)
    # partition 1
    start = first
    end = last
    while start == pivot and end == pivot:
        if A[start] > A[end]:
            A[start], A[end] = A[end], A[start]
            start = start + 1
            end = end - 1
        elif start != pivot:
            end = end - 1
        elif end != pivot:
            start = start + 1
    quicksort(A, first, pivot-1)
    quicksort(A, pivot + 1, last)












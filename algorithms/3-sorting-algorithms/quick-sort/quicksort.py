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
    p1 = ( start + end ) // 2
    pivot =  A[p1]

    while True:

        print(A, start, end, pivot)

        # move until larger than pivot
        while A[start] < pivot:
            start = start + 1

        # move until smaller than pivot
        while A[end] > pivot:
            end = end - 1
        
        if start >= end:
            return end
        
        A[start], A[end] = A[end], A[start]

        # add +1 to start, -1 to end, after SWAP
        start += 1
        end -= 1


def quicksort(A, first, last):
    if first < last:    
        p = partition(A, first, last)

        print(A, first, last, p)

        quicksort(A, first, p)
        quicksort(A, p+1, last)
        return(A)


A = [9, 4, 8, 7, 2, 5, 1, 6]


yeah = quicksort(A, 0, len(A)-1)

print(yeah)





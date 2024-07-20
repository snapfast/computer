# binary search - searching technique

inp = [4, 5, 6, 8, 12, 33, 54, 66, 78]

search = 12

l = len(inp)

# search list must be sorted
def binary_search(data, low, high, query):

    while low <= high:
        mid = low + (high - low) // 2

        if query == data[mid]:
          return mid+1
        elif data[mid] < query:
          low = mid + 1
        else:
          high = mid - 1

    return -1

print(binary_search(inp, 0, l, search))




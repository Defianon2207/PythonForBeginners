#Merge Sorting every beginner should try this as this will trigger teir thinking power and also help to understand 
#how recussion is helpul instead of using mulitple if and else

def mid_break(_args):
    if len(_args) <= 1:
        return _args
    mid = len(_args) // 2
    left = mid_break(_args[:mid])
    right = mid_break(_args[mid:])
    print("Left",left)
    print("right",right)
    return _merge(left,right)

def _merge(_left,_right):
    result =[]
    i=0
    j=0
    while i < len(_left) and j < len(_right):
        if _left[i] <= _right[j]:
            result.append(_left[i])
            i += 1
        else:
            result.append(_right[j])
            j += 1
    result.extend(_left[i:])
    result.extend(_right[j:])
    return result


def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]

    # Index of the smaller element
    i = low - 1

    # Rearrange elements around the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the left part
        quick_sort(arr, low, pivot_index - 1)

        # Recursively sort the right part
        quick_sort(arr, pivot_index + 1, high)







def main():
    arr = 82744627829274869
    arr = [int(d) for d in str(arr)]
    quick_sort(arr, 0, len(arr) - 1)
    print("After :", arr)

main()

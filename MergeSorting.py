def merge_sort(arr):
    # Base case: A list with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the list
    mid = len(arr) // 2

    # Divide the list into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def main():
    arr = 82744627829274869
    arr = [int(d) for d in str(arr)]
    print(merge_sort(arr))

main()

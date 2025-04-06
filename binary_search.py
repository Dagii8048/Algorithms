def binarySearch(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]: 
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

nums = list(map(int, input("Enter the list of numbers: ").split()))
target = int(input("Enter the target number you want to find in the list: "))

print(f"The index of this number is the sorted array {binarySearch(nums, target)}.")
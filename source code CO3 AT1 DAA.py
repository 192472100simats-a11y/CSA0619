import time

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def main():

    print("=" * 60)
    print("BINARY SEARCH PERFORMANCE IN REAL-TIME SYSTEMS")
    print("=" * 60)

    n = int(input("Enter Number of Elements : "))

    arr = []

    print("\nEnter Elements in Sorted Order")

    for i in range(n):
        arr.append(int(input()))

    target = int(input("\nEnter Target Element : "))

    start = time.perf_counter()

    result = binary_search(arr, target)

    end = time.perf_counter()

    execution_time = end - start

    print("\n" + "=" * 60)

    if result != -1:
        print("Element Found at Position :", result + 1)
    else:
        print("Element Not Found")

    print("Execution Time : {:.8f} seconds".format(execution_time))
    print("Best Case Time Complexity    : O(1)")
    print("Average Time Complexity      : O(log n)")
    print("Worst Case Time Complexity   : O(log n)")
    print("=" * 60)


main()

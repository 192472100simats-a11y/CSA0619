# Q19 - Debugging and Optimization Task
# Pair Sum (Optimized Brute Force)

def pair_sum(arr, target):

    comparisons = 0

    print("\nSearching for Pair...\n")

    for i in range(len(arr)):

        for j in range(i + 1, len(arr)):

            comparisons += 1

            print("Checking Pair :", arr[i], "+", arr[j])

            if arr[i] + arr[j] == target:

                print("\nPair Found Successfully!")
                print("First Element :", arr[i])
                print("Second Element :", arr[j])
                print("Indices :", i, j)
                print("Target Sum :", target)
                print("Total Comparisons :", comparisons)

                return

    print("\nPair Not Found")
    print("Total Comparisons :", comparisons)


def main():

    print("=" * 60)
    print("DEBUGGING AND OPTIMIZATION - PAIR SUM")
    print("=" * 60)

    n = int(input("Enter Number of Elements : "))

    arr = []

    print("\nEnter Array Elements")

    for i in range(n):
        element = int(input("Element {} : ".format(i + 1)))
        arr.append(element)

    target = int(input("\nEnter Target Sum : "))

    print("\nArray :", arr)
    print("Target :", target)

    pair_sum(arr, target)

    print("\n" + "=" * 60)
    print("Optimization Applied")
    print("- Duplicate comparisons removed")
    print("- Self comparisons avoided")
    print("- Inner loop starts from i + 1")
    print("\nTime Complexity : O(n^2)")
    print("Space Complexity : O(1)")
    print("=" * 60)


main()

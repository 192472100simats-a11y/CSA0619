# Q19: Employee Salary Search Using Binary Search

def binary_search(salaries, target):

    low = 0
    high = len(salaries) - 1
    comparisons = 0

    while low <= high:

        mid = (low + high) // 2
        comparisons += 1

        print("\nComparison", comparisons)
        print("Middle Position :", mid + 1)
        print("Salary at Middle :", salaries[mid])

        if salaries[mid] == target:
            return mid, comparisons

        elif salaries[mid] < target:
            print("Searching Right Half...")
            low = mid + 1

        else:
            print("Searching Left Half...")
            high = mid - 1

    return -1, comparisons


def main():

    print("=" * 60)
    print("EMPLOYEE SALARY SEARCH USING BINARY SEARCH")
    print("=" * 60)

    n = int(input("Enter Number of Employee Salary Records : "))

    salaries = []

    print("\nEnter Salaries in Sorted Order")

    for i in range(n):
        salary = int(input("Salary {} : ".format(i + 1)))
        salaries.append(salary)

    print("\nSalary Records")
    print(salaries)

    target = int(input("\nEnter Salary to Search : "))

    position, comparisons = binary_search(salaries, target)

    print("\n" + "=" * 60)

    if position != -1:
        print("Salary Found")
        print("Position :", position + 1)
        print("Salary :", salaries[position])
    else:
        print("Salary Not Found")

    print("Total Comparisons :", comparisons)
    print("Best Case Time Complexity    : O(1)")
    print("Average Time Complexity      : O(log n)")
    print("Worst Case Time Complexity   : O(log n)")
    print("=" * 60)


main()

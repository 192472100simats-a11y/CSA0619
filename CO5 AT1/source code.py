# Q19 - Bin Packing Problem
# Backtracking with Pruning

items = [7, 5, 6, 4, 2, 3]
bin_capacity = 10

# Sort items in decreasing order
items.sort(reverse=True)

best_solution = []
minimum_bins = len(items)


def bin_packing(index, bins):

    global best_solution
    global minimum_bins

    # Pruning: current solution already uses
    # more bins than the best solution
    if len(bins) >= minimum_bins:
        return

    # All items have been packed
    if index == len(items):

        minimum_bins = len(bins)

        best_solution = [bin.copy() for bin in bins]

        return

    item = items[index]

    used_loads = set()

    # Try placing the item in existing bins
    for i in range(len(bins)):

        current_load = sum(bins[i])

        # Symmetry pruning
        if current_load in used_loads:
            continue

        used_loads.add(current_load)

        # Capacity constraint
        if current_load + item <= bin_capacity:

            bins[i].append(item)

            bin_packing(index + 1, bins)

            # Backtracking
            bins[i].pop()

    # Try creating a new bin
    if len(bins) + 1 < minimum_bins:

        bins.append([item])

        bin_packing(index + 1, bins)

        bins.pop()


def main():

    global minimum_bins

    print("=" * 60)
    print("BIN PACKING PROBLEM")
    print("BACKTRACKING WITH PRUNING")
    print("=" * 60)

    print("\nItems:", items)

    print("Bin Capacity:", bin_capacity)

    # Initial upper bound:
    # each item can be placed in a separate bin
    minimum_bins = len(items) + 1

    bin_packing(0, [])

    print("\nOPTIMAL BIN ALLOCATION")
    print("-" * 60)

    for i, bin_items in enumerate(best_solution, start=1):

        print(
            "Bin", i,
            ":", bin_items,
            "| Total =", sum(bin_items)
        )

    print("\nMinimum Number of Bins:", minimum_bins)

    print("\nConstraints Satisfied:")

    print("1. Every item is assigned exactly once.")

    print("2. No bin exceeds capacity.")

    print("3. Number of bins is minimized.")

    print("=" * 60)


main()

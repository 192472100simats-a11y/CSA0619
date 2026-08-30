# Q19 - Independent Set Problem
# Maximum Independent Set Using Backtracking


graph = [

    [0, 1, 0, 1, 0],

    [1, 0, 1, 0, 0],

    [0, 1, 0, 1, 0],

    [1, 0, 1, 0, 1],

    [0, 0, 0, 1, 0]

]


n = len(graph)

best_set = []


# Function to check whether a vertex
# can be added to the current independent set

def is_safe(vertex, current_set):

    for selected_vertex in current_set:

        if graph[vertex][selected_vertex] == 1:

            return False

    return True


# Backtracking function

def backtrack(vertex, current_set):

    global best_set


    # Base case

    if vertex == n:

        if len(current_set) > len(best_set):

            best_set = current_set.copy()

        return


    # Pruning condition

    remaining_vertices = n - vertex

    if len(current_set) + remaining_vertices <= len(best_set):

        return


    # Include the vertex if it is safe

    if is_safe(vertex, current_set):

        current_set.append(vertex)

        backtrack(vertex + 1, current_set)

        # Backtracking

        current_set.pop()


    # Exclude the current vertex

    backtrack(vertex + 1, current_set)


def main():

    print("=" * 60)

    print("MAXIMUM INDEPENDENT SET PROBLEM")

    print("USING BACKTRACKING WITH PRUNING")

    print("=" * 60)


    print("\nAdjacency Matrix:\n")


    for row in graph:

        print(row)


    # Start Backtracking

    backtrack(0, [])


    print("\nMaximum Independent Set:", best_set)

    print("Maximum Independent Set Size:", len(best_set))


    print("\nVerification:")


    print("No two selected vertices are directly connected.")

    print("All independent set constraints are satisfied.")


    print("=" * 60)


main()

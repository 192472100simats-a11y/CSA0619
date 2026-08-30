# Q19 - Floyd's Algorithm vs Warshall's Algorithm
# Dynamic Programming Comparison


INF = 99999


# Floyd's Algorithm
def floyd_algorithm(graph):

    n = len(graph)

    distance = []

    for row in graph:
        distance.append(row.copy())

    for k in range(n):

        for i in range(n):

            for j in range(n):

                if distance[i][k] + distance[k][j] < distance[i][j]:

                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


# Warshall's Algorithm
def warshall_algorithm(graph):

    n = len(graph)

    reachability = []

    for row in graph:
        reachability.append(row.copy())

    for k in range(n):

        for i in range(n):

            for j in range(n):

                reachability[i][j] = (
                    reachability[i][j]
                    or
                    (reachability[i][k] and reachability[k][j])
                )

    return reachability


# Function to print matrix
def print_matrix(matrix):

    for row in matrix:

        for value in row:

            if value == INF:
                print("INF", end="\t")

            else:
                print(value, end="\t")

        print()


def main():

    print("=" * 65)
    print("FLOYD'S ALGORITHM VS WARSHALL'S ALGORITHM")
    print("DYNAMIC PROGRAMMING COMPARISON")
    print("=" * 65)


    # Weighted Graph for Floyd's Algorithm

    weighted_graph = [

        [0, 3, INF, 7],

        [8, 0, 2, INF],

        [5, INF, 0, 1],

        [2, INF, INF, 0]

    ]


    print("\nWEIGHTED ADJACENCY MATRIX")

    print_matrix(weighted_graph)


    # Floyd's Algorithm

    shortest_paths = floyd_algorithm(weighted_graph)


    print("\nSHORTEST PATH MATRIX USING FLOYD'S ALGORITHM")

    print_matrix(shortest_paths)


    # Graph for Warshall's Algorithm

    adjacency_graph = [

        [1, 1, 0, 1],

        [1, 1, 1, 0],

        [1, 0, 1, 1],

        [1, 0, 0, 1]

    ]


    print("\nADJACENCY MATRIX")

    print_matrix(adjacency_graph)


    # Warshall's Algorithm

    transitive_closure = warshall_algorithm(adjacency_graph)


    print("\nTRANSITIVE CLOSURE USING WARSHALL'S ALGORITHM")

    print_matrix(transitive_closure)


    print("\n" + "=" * 65)

    print("COMPLEXITY ANALYSIS")

    print("=" * 65)

    print("Floyd's Algorithm Time Complexity    : O(n^3)")

    print("Warshall's Algorithm Time Complexity : O(n^3)")

    print("Space Complexity                     : O(n^2)")

    print("=" * 65)


main()

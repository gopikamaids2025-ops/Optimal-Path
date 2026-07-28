from itertools import permutations

INF = float('inf')


def tsp_brute_force(cost, n):
    """Find the optimal TSP tour using brute force."""

    cities = list(range(1, n))
    best_cost = INF
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]

        total_cost = 0
        valid = True

        for i in range(n):
            if cost[path[i]][path[i + 1]] == INF:
                valid = False
                break
            total_cost += cost[path[i]][path[i + 1]]

        if valid and total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


# ---------------- Main Program ----------------

n = int(input("Enter the number of cities: "))

cities = []
for i in range(n):
    cities.append(chr(65 + i))  # A, B, C, D...

print("\nEnter the cost matrix:")
print("Enter -1 for no direct path (Diagonal will be INF).\n")

cost = []

for i in range(n):
    row = []
    for j in range(n):

        if i == j:
            row.append(INF)
        else:
            value = int(input(f"Cost from {cities[i]} to {cities[j]}: "))
            if value == -1:
                row.append(INF)
            else:
                row.append(value)

    cost.append(row)

# Solve TSP
best_path, best_cost = tsp_brute_force(cost, n)

# Display Cost Matrix
print("\nCost Matrix:\n")

print("    ", end="")
for city in cities:
    print(f"{city:>6}", end="")
print()

for i in range(n):
    print(f"{cities[i]:>4}", end="")
    for j in range(n):
        if cost[i][j] == INF:
            print(f"{'INF':>6}", end="")
        else:
            print(f"{cost[i][j]:>6}", end="")
    print()

# Display Result
if best_path:
    print("\nOptimal Tour:")
    print(" -> ".join(cities[i] for i in best_path))

    print("\nMinimum Cost:", best_cost)

    print("\nPath Verification:")
    for i in range(n):
        u = best_path[i]
        v = best_path[i + 1]
        print(f"{cities[u]} -> {cities[v]} : Cost = {cost[u][v]}")
else:
    print("\nNo valid tour found.")
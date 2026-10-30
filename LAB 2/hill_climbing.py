def objective(x):
    return -(x - 5)**2 + 25


def hill_climbing(start):
    current = start

    while True:
        neighbors = [current - 1, current + 1]

        best = current

        for n in neighbors:
            if objective(n) > objective(best):
                best = n

        if best == current:
            break

        current = best

    return current


start = 0

result = hill_climbing(start)

print("Best state:", result)
print("Maximum value:", objective(result))

def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    # Check whether the goal is already a known fact
    if goal in facts:
        print("Fact found:", goal)
        return True

    # Avoid infinite loops caused by cyclic rules
    if goal in visited:
        print("Cycle detected:", goal)
        return False

    visited = visited | {goal}

    # Search for rules that can prove the goal
    for conditions, conclusion in rules:
        if conclusion == goal:
            print("Trying to prove:", goal)

            # All conditions must be proved
            if all(
                backward_chaining(
                    condition, facts, rules, visited
                )
                for condition in conditions
            ):
                print("Proved:", goal)
                return True

    print("Cannot prove:", goal)
    return False


# Known facts
facts = {"A", "B"}

# Rules: (conditions, conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

# Goal to prove
goal = "E"

print("Goal:", goal)

if backward_chaining(goal, facts, rules):
    print("Goal successfully proved.")
else:
    print("Goal could not be proved.")
def forward_chaining(facts, rules, goal):
    facts = set(facts)

    print("Initial facts:", facts)

    while True:
        new_fact_added = False

        for conditions, conclusion in rules:
            # Check whether all conditions are true
            if set(conditions).issubset(facts):

                # Add the conclusion if it is not already known
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("Inferred:", conclusion)
                    new_fact_added = True

        # Check whether the goal has been achieved
        if goal in facts:
            print("Goal achieved:", goal)
            return True

        # Stop if no new facts can be inferred
        if not new_fact_added:
            break

    print("Goal cannot be proved:", goal)
    return False


# Initial facts
facts = ["A", "B"]

# Rules: (conditions, conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

# Goal to prove
goal = "E"

forward_chaining(facts, rules, goal)
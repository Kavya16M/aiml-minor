# ---------- FORWARD CHAINING ----------

def forward_chaining(facts, rules):
    inferred = set(facts)
    result = []

    changed = True
    while changed:
        changed = False
        for condition, conclusion in rules:
            if condition.issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                result.append(conclusion)
                changed = True

    return result


# ---------- BACKWARD CHAINING ----------

def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        return True

    if goal in visited:
        return False

    visited.add(goal)

    for condition, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(c, facts, rules, visited) for c in condition):
                return True

    return False


# ---------- RESOLUTION STRATEGY ----------

def resolve(ci, cj):
    resolvents = []
    for literal in ci:
        if literal.startswith("~"):
            complementary = literal[1:]
        else:
            complementary = "~" + literal

        if complementary in cj:
            new_clause = (ci - {literal}) | (cj - {complementary})
            resolvents.append(new_clause)

    return resolvents


def resolution(clauses):
    clauses = [set(c) for c in clauses]

    while True:
        new = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = resolve(clauses[i], clauses[j])

                for r in resolvents:
                    if not r:
                        return True
                    new.append(r)

        if all(r in clauses for r in new):
            return False

        clauses.extend(new)


# ---------- KNOWLEDGE BASE ----------

facts = {"A"}

rules = [
    ({"A"}, "B"),
    ({"B"}, "C"),
    ({"C"}, "D")
]

goal = "D"

clauses = [
    {"A"},
    {"~A", "B"},
    {"~B", "C"},
    {"~C", "D"},
    {"~D"}
]


# ---------- EXECUTION ----------

forward_result = forward_chaining(facts, rules)
backward_result = backward_chaining(goal, facts, rules)
resolution_result = resolution(clauses)


print("forward_chaining_result:", forward_result)
print("backward_chaining_result:", backward_result)
print("resolution_result:", resolution_result)

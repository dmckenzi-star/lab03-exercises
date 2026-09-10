# AI use disclosure: ChatGPT assisted with Python syntax and translating my set-based Java solution.


def check(values: list) -> bool:
    seen = set()

    for value in values:
        if value in seen:
            return True
        seen.add(value)

    return False


print(check([1, 2, 3, 2]))
print(check([5, 2, -10, 44, 90]))

additional_values = [10, 20, 30, 10]
expected = True
actual = check(additional_values)
print(
    f"Additional test: input={additional_values}, expected={expected}, actual={actual}, "
    f"{'PASS' if actual == expected else 'FAIL'}"
)

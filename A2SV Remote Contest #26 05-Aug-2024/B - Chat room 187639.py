# Problem: B - Chat room - https://codeforces.com/gym/540348/problem/B

def func(s):
    target = "hello"
    pointer = 0

    for char in s:
        if char == target[pointer]:
            pointer += 1
        if pointer == len(target):
            return "YES"

    return "NO"


s = input()
print(func(s))

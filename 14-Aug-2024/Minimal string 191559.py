# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

def minimal_string_game(s):
    stack = []
    result = []
    min_char = [chr(ord('z') + 1)] * (len(s) + 1)
    for i in range(len(s) - 1, -1, -1):
        min_char[i] = min(s[i], min_char[i + 1])
    
    for i, char in enumerate(s):
        stack.append(char)
        while stack and stack[-1] <= min_char[i + 1]:
            result.append(stack.pop())
    result.extend(reversed(stack))
    
    return ''.join(result)
s = input().strip()
result = minimal_string_game(s)
print(result)
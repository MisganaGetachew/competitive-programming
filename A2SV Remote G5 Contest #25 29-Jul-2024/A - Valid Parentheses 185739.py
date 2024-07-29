# Problem: A - Valid Parentheses - https://codeforces.com/gym/537575/problem/A

s = input()
stack = []
unmatched = 0

for chr in s:
    if chr == '(':
        stack.append(chr)
    elif chr == ')':
        if stack:
            stack.pop()
        else:
            unmatched += 1

unmatched += len(stack)
mx = len(s) - unmatched
print(mx)

n, q = map(int, input().split())
words = list(map(str, input().split()))
words = {word: idx for idx, word in enumerate(words)}
for _ in range(q):
    ans = []
    pref, suff = input().split()

    for word in words:
        if word[len(word)-len(suff):] == suff and word[:len(pref)] == pref:
            ans.append(words[word])

    if len(ans):
        print(max(ans))
    else:
        print(-1)

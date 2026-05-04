n = int(input())
names = []
for _ in range(n):
    name = input()
    names.append(name)

alphabet = "abcdefghijklmnopqrstuvwxyz"
adj = {char : [] for char in alphabet}
in_degree = {char: 0 for char in alphabet}

possible = True
for i in range(n-1):
    word1 = names[i]
    word2 = names[i+1]

    difference = False
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            adj[char1].append(char2)
            in_degree[char2] += 1
            difference = True
            break
    if not difference and len(word1) > len(word2):
        possible = False
if not possible:
    print("Impossible")
else:
    zeropreq = []
    for char in alphabet:
        if in_degree[char] == 0:
            zeropreq.append(char)
    
    result = []
    while zeropreq:
        current = zeropreq.pop()
        result.append(current)

        for child in adj[current]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                zeropreq.append(child)

    if len(result) < 26:
        print("Impossible")

    else:
        print("".join(result))
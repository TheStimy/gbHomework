src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

while len(src):
    tmp = src[0]
    src.remove(src[0])
    if tmp not in src:
        result.append(tmp)
    else:
        while tmp in src:
            src.remove(tmp)

print(result)

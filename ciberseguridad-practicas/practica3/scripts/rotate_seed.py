seed = "srrqnn"
prefix = "6931fac9da"
sufix = "b2b36c248b"

for i in range(26):
    b = ""
    for j in seed:
        b += chr(((ord(j) - 97 + i) % 26) + 97)
    print(f'{i}\t{prefix + b + sufix}')
    #print(f'{i}\t{b}')

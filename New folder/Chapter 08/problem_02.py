def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
names = ["Ahad", "Ahmad", "Ali"]

print(rem(names, "ad"))
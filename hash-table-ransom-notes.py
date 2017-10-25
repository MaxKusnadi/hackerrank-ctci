def ransom_note(magazine, ransom):
    d = dict()
    for word in magazine:
        val = d.get(word)
        if val:
            d[word] += 1
        else:
            d[word] = 1
    for word in ransom:
        val = d.get(word)
        if not val:
            return False
        if val < 1:
            return False
        d[word] -= 1
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

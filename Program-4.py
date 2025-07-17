def key_multiples(li):
    dic = {}
    for key in range(1,10):
        dic[key] = 0
    for value in li:
        for key in dic:
            if value%key == 0:
                dic[key] += 1
    return dic
li = list(map(int,input("Enter the numbers: ").split()))
print(key_multiples(li))
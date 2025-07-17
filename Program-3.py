def series2(n):
    li = []
    if n%2 !=0 :
        x = n
    else:
        x = n-1
    for i in range(x):
        li.append(2*i+1)
    return li
n = int(input("Enter the number: "))
print(series2(n))
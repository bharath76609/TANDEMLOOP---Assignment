def series1(n):
    li = []
    for i in range(n):
        li.append(2*i+1)
    return li
n = int(input("Enter the number: "))
print(series1(n))
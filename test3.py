lists = [[1,4,5], [1,3,4], [2,6]]
lst1 = []
for i in lists:
    for j in i:
        lst1.append(j)
for k in range(len(lst1)):
    for l in range(k,len(lst1)):
        if lst1[k] > lst1[l]:
            lst1[k],lst1[l] = lst1[l],lst1[k]
print(lst1)

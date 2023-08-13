a=[6,8,9,5,4,3,11,1]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[j],a[i]=a[i],a[j]
print(a)

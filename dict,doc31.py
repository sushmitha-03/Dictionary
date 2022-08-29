
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
data={"item1": 45.50, "item2":35, "item3": 41.30, "item4":55, "item5":24}
a=[]
for b in data:
    a.append(data[b])
max1=0
for i in (range(len(a))):
    if a[i]>max1:
        max1=a[i]
max2=0
for j in (range(len(a))):
    if a[j]>max2:
        max2=a[i]
max3=0
for k in (range(len(a))):
    if a[k]>max3:
        max3=a[i]
print("item1",max1)
print("item2",max2)
print("item3",max3)


dict1={"I","LOVE","YOU"}
dict2={1,4,3}
dict3={}
for i in dict1:
    for j in dict2:
        dict3[i]=j
        dict2.remove(j)
        break
print(dict3)
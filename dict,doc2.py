a= 'w3resource'
b=list(a)
c={}
for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
# {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

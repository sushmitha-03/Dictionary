a={"s":1,"u":2,"s":3,"h":4,"m":5}
l=list(a.keys())
l.sort()
dic={}
for i in l:
    dic[i]=a[i]
print(dic)
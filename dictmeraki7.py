list=[{"first":1},{"second":2},{"third":1},{"four":5},{"five":5},{"six":9},{"seven":7}]
x=[]
a=[]
for i in list:
    for j in i.values():
        if j not in a:
            a.append(j)
print(a)


 
# a='Roshni'
# dict={}
# for i in a:
#     dict[i]=a
# print(dict)

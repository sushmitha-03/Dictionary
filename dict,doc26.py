# Sample Output:

# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

a= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in a:
    print(i,end=" ")
print()
b=[]
for i in a:
    b2=a[i]
    b.append(b2)

for l in range(len(b)):
    # print(l)
    for i2 in range(len(b[l])):
        print(b[l][i2],end=" ")
    print()


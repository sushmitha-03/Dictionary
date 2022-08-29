

# dict={1:10,3:40,5:20,2:20,6:50}
# l=list(dict.values())
# max=0
# i=0
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#     i+=1
# print=l[0]
# min=l[0]
# for i in l:
#     if i<min:
#         min=1
# print(max,min)

my_dict ={1:10,3:40,5:20,2:20,6:50}
l=list(my_dict.values())
i=0
max1=0
while i<len(l):
     if l[i]>max1:
         max1=l[i]
     i+=1
print(max1)
my_dict ={1:10,3:40,5:20,2:20,6:50}
l=list(my_dict.values())
i=0
min=l[0]
for i in l:
    if i<min:
        min=1
print(min)

a={'c1': 'Red', 'c2':'green', 'c3':None }
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
dic={}
a.popitem()
print(a)
# for i in a:
#     if a[i]==None:
#         a.pop(i)
# print(a)

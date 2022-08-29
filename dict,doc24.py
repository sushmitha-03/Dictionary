from collections import Counter
dict= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
a= Counter()
for d in dict:
    a[d['item']] += d['amount']
print(a)

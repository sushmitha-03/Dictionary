dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
b=[]
for i in dic:
	for j in i.values():
		b.append(j)
print(set(b))



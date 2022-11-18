tup = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

first_list =[]
second_list =[]

for a in tup:
    first_list.append(a[1],)

first_list.sort()


for l in first_list:
    for r in tup:
        if l == int(r[1],):
            second_list.append(r)

print(second_list)

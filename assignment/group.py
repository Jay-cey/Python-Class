# Grouping Algorithm

list_of_items = ['ada', 'bello', 'mercy', 'pierce', 'taylor', 'kane', 'lorem', 'ipsum', 'dolor']
group1 = []
group2 = []
for i in list_of_items:
    if list_of_items.index(i) % 2 == 0:
        group1.append(i)
    else:
        group2.append(i)

print(f"group 1 members: {group1}")
print(f"group 2 members: {group2}")
print("group 1 members: ", *group1, sep=', ')
print("group 2 members: ", *group2, sep=', ')
# print(*group1)
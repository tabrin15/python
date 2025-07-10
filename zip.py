m1 = {2, 3, 1}
m2 = {'b','a','c'}
m3 = list(zip(m1,m2))   
print()
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90,]
list2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]

for x, y in zip(list1, list2):
    print(x, y)
print()

for x, y in zip(list1, list2[::-1]):
    print(x,y)

print()
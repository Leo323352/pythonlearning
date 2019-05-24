#list
x = [1, 2, -3, -3, 2, 1]
y = [4, 5, 6]

#the difference between append and extend 
x.append(y)
print(x)
#extend
x.extend(y)
print(x)
#count
n = x.count(2)
print(n)
#index
i = x.index(1, 0, 2)
print(i)
#insert
x.insert(1,10)
print(x)
#pop
x.pop(1)
print(x)
#remove
x.remove(y)
print(x)
#sort
x.sort()
print(x)

items = [{'name' : 'leo', 'age' : 19},{'name' : 'James', 'age':18}, {'name': 'che', 'age':17}]
items.sort(key = lambda s : s.get('age'), reverse = True)
print(items)
#reverse
x.reverse()
print(x)
#empty

if x != []:
	print('非空列表')






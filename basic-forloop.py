import time

print(list(range(1,10+1)))
for i in range (10):
	print(i)
print('================')
for i in range (1,11):
	print(i)
	print('-----------')
print('================')

for i in range (1,10,2):
	print(i)
	time.sleep(1)
	print('-----------')

print('================')

friend = ['Alberd', 'Steve', 'Ada', 'Edison']
for f in friend:
	print(f)
print('================')

friend = ['Alberd', 'Steve', 'Ada', 'Edison']
for f in friend:
	if f == 'Alberd':
		print(f)

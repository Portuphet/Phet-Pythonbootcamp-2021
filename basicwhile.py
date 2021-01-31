money = 998
transfer = 2000
service_charge = 15

cost = transfer+service_charge

# print('Condition: ', money < transfer)
print('Would be transfer', transfer, 'Service Charge 15')
while money < cost:
	print('You have money ', money)
	print ('Out of balance, Please transfer money into account')
	getmoney = int(input('How much deposit money: '))
	money = money + getmoney 
	print('---')

print('You have money', money)
print('Transfer Money!!')
print('Total balance: ', money - cost)
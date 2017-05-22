print('*** Welcome to grade central *** \n')
print('Please login: \n')
name = input('Name: ')
password = input('Password: ')

if name != 'admin':
    print('No access')
    exit()
if password != 'leren':
    print('No access')
    exit()
else:
	print("\n" * 80)
	print('Welcome to grade central \n')
	print('[1] - Enter grades')
	print('[2] - Remove student')
	print('[3] - Student Average grades')
	print('[4] - Exit \n')
	keuze = input('What would you like to do today?: ')

if keuze == 4: 
	exit()











password = input()
if password == 'test':
    print('Access granted!')
else:
    print('Wrong password!!')

print('But whats your name?')
name = input()
print('Hi,' + name + " what about your age?")
age = int(input())
if age < 18:
    print('WTF r u doing here buddy? get away!')
elif age >= 18 and age < 60:
    print('Welcome, the password is \'test\'!')
else:
    print('GRANDPA?')

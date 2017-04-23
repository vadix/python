os = ['linux', 'mac os', 'windows']
print(os)
print(os[0])
print(os[0].title())
print(os[-1])
print('My first OS was a ' + os[-1].title() + '!')
os.append('ZX spectrum')
print(os)
os.insert(0, 'dos')
os.insert(1, 'os/2')
print(os)
del os[1]
print(os)
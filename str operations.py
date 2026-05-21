name='pyneni harsha'
#print(name)
print(name[0]) # index of 0 is 'p'

age='22'
print(name+''+age)
print(name[0:6]) # index 0 to 5 is 'pyneni'
print(name[0:])
print(name[:9])
print(name[0:6:1])
print(name[0:6:2])
print(name[0:1])
print(name[3:])
print(name[:6])
print(name[::2])
print(name[-1])
#print(name[-1:-7])
print(name[-7:-1])
print(name[-9:-3])

name =str(input())
batch='spark'
type='fellowship'
duration='4'
print('attar')
print('welcome to algonex!')
print('welcome to algonex'+' '+name+' '+batch+' '+type+' '+duration+' ')

print(f'welcome to algonex\t{name}\tyour batch\t{batch}\tyour type\t{type}\twith duration\t{duration}')

print("hello\t{}\tyour's is{}batch for {}".format(name,batch,type))

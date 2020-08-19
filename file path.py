import os.path
if os.path.isfile('yee.txt'):
    print('yes')
    f = open('yee.txt','a')
    f.write('yes')
else:
    print('no')
    f = open('yee.txt','w')
    f.write('no')
f.close()
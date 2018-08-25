import os
import binascii

with open('二进制文件.dat','rb') as f:
    content = f.read()
hexstr = binascii.b2a_hex(content)
print('1',content)
print('2',hexstr)
string = binascii.a2b_hex(hexstr)
print('3',string)
print('4',bytes(string))
with open('还是二进制文件.dat','wb') as f:
    content = f.write(string)
import os
os.system('cls')

ascii_list = []
six_digit_binary_list = []
temp_list = []
base64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
final_str =''
binary_str = ''
pay_load = ''


encoded_str = input("Enter :")

for i in encoded_str:
    ascii_list.append(ord(i))


for i in ascii_list:
    if 48 >= i or i<=57:
        binary_str += (''.join(bin(i)).replace('b','0'))
    else:
        binary_str += (''.join(bin(i) ).replace('b',''))


for bit in range(0,len(binary_str),6):
    six_digit_binary_list.append(binary_str[bit:bit + 6])

for i in six_digit_binary_list:
    if len(i) == 2:
        i += '0000'
        pay_load += '=='
    elif len(i) == 4:
        i += '00'
        pay_load += '=' 
    temp_list.append(int(i,2))

for i in temp_list:
    final_str += base64_table[i]

final_str += pay_load
        
print(final_str)

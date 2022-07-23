first_list = ['red', 'white','yellow']
second_list = ['green', 'blue','red', 'white']
flag = False
for i in first_list:
    if i in second_list:
        flag = True
        break
print(flag)
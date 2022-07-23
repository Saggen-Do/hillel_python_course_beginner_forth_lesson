initial_tuple = (1, 2, 3)
initial_list = []
for i in initial_tuple:
    initial_list.append(i)
initial_list.pop()
final_tuple = tuple(initial_list)
print(final_tuple)
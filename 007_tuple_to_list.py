tuples_in_list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
lists_in_list = []
while len(tuples_in_list)!=0:
    each_tuple = tuples_in_list.pop()
    each_list = []
    for x in each_tuple:
        each_list.append(x)
    lists_in_list.append(each_list)
lists_in_list.reverse()
print(lists_in_list)
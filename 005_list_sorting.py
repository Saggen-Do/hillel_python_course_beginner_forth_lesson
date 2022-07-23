initial_insert = ['red', 'white', 'black', 'red', 'green', 'black']
# sorted_list = initial_insert.sort()
final_list_with_no_duplicates = []
for color in initial_insert:
    if color not in final_list_with_no_duplicates:
        final_list_with_no_duplicates.append(color)
final_list_with_no_duplicates.sort()
print(final_list_with_no_duplicates)
list_of_pruducts =  ['bread', 'milk', 'kolbasa']
max_length_item = max(list_of_pruducts, key=len)
len_count = len(max_length_item)
final_result = 'Самое длинное название продукта {} длинна {} символов'.format(max_length_item, len_count)
print(final_result)
initial_string = ('Hillel school')
string_list = list(initial_string)
character_dict = {i:string_list.count(i) for i in string_list};
print(character_dict)
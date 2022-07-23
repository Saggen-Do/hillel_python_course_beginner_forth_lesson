initial_string = ( 'Hillel school')
string_length = len(initial_string)
if string_length<2:
    print('Your string is too short')
else:
    first_part = initial_string[:2:]
    second_part = initial_string[string_length-2::]
    final_result = (first_part+second_part)
    print(final_result)
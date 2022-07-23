import unicodedata
initial_sequence = list(range(-99,99,3))
for each_element in initial_sequence:
    if each_element%3==0:
        result = each_element
        print(f"Number {result} devided on 3")
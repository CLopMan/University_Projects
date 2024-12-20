flag = "7337614609fdcbzz732a7d000fb1a414"
num_rotations = 1
letters_to_number = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
number_to_letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}
new_flag = ""

for i in range(len(flag)):
    c = flag[i]
    if c.isnumeric():
        new_c = (int(c) - num_rotations) % 10
    elif c in letters_to_number.keys():
        new_c = number_to_letters[(letters_to_number[c] - num_rotations) % 6]
    else:
        new_c = c
    new_flag += str(new_c)

print(new_flag)

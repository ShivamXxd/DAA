def length_of_string(s):
    if s == '':
        return 0
    return 1 + length_of_string(s[1:])

print(length_of_string("hello"))

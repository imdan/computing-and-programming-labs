def remainingwords(s):
    first_space_index = 0
    for char in s:
        if (char != " "):
            first_space_index += 1
        else:
            break
    return s[first_space_index + 1:]

# s = input()

# print(remainingwords(s))

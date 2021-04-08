def firstword(s):
    first_word = ''
    for char in s:
        if (char != " "):
            first_word = first_word + char
        else:
            break
    return first_word

# s = input()

# first = firstword(s)

# print(first, 'is the first word')

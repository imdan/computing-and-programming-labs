def max_abs_val(lst):
    for i in range(len(lst)):
        lst[i] = abs(lst[i])
    max_value = max(lst)
    return max_value

# lst = [-190, -3, 20, -1, 0, -25]

# print(max_abs_val(lst))
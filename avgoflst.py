def avg_val(lst):
    total = 0
    for elem in lst:
        total = total + elem
    average = total / len(lst)
    return average

# lst = [19, 2, 20, 1, 0, 18]

# print(avg_val(lst))
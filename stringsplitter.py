print("Enter an odd length string:")

line = input()

middle_ind = int(len(line)/2)
middle_char = line[middle_ind]

first_half = line[:middle_ind]
second_half = line[middle_ind+1:]

print('Middle character:', middle_char)
print('First half: ', first_half)
print('Second half:', second_half)

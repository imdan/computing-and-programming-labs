print('Please enter a positive integer:')

n = int(input())

count = 0
i = 1

while(count < n):
    if(i % 2 == 0):
        print(i)
        i += 1
        count += 1
    else:
        i += 1

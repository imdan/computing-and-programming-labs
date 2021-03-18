print('Please enter a positive integer greater than 1: ')

n = int(input())

count = 0
first = 1
second = 1
current = 0

while(count < n):
    print(first)
    current = first + second
    first = second
    second = current
    count += 1

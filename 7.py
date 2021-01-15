""" Project Euler #7: 10001st prime """

numbers = set(range(3, 105000, 2))
for i in range(3, 325):
    if i not in numbers:
        continue
    num = i
    while(num < 105000):
        num += i
        if num in numbers:
            numbers.remove(num)
numbers.add(2)
numbers = sorted(numbers)

t = int(input())
while (t > 0):
    n = int(input())
    result = numbers[n-1]
    print(result)
    t -= 1

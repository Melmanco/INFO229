def fizzbuzz(n):
    result = ''

    if (n % 3 == 0) or ('3' in str(n)):
        result += 'Fizz'

    if (n % 5 == 0) or ('5' in str(n)):
        result += 'Buzz'

    if result == '':
        print(n)

    else:
        print(result)

for i in range(1,101):
    fizzbuzz(i)
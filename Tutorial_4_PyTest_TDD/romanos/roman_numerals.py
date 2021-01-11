def convert(num, num_type):

    if num_type == 'num':
        return {
            1000: 'M',
            900: "CM",
            500: 'D',
            400: "CD",
            100: 'C',
            90: "XC",
            50: 'L',
            40: "XL",
            10: 'X',
            9: "IX",
            5: 'V',
            4: 'IV',
            1: 'I'
    }[num]

    elif num_type == 'rom':
        return {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }[num]

def numberToRoman(num):
    stack = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''

    while num > 0:
        if num < stack[0]:
            stack = stack[1:]
        else:
            result += convert(stack[0], 'num') 
            num -= stack[0]
    
    return result

def romanToNumber(rom):
    stack = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = 0

    while rom > '':
        if not rom.startswith(stack[0]):
            stack = stack[1:]
        else:
            result += convert(stack[0], 'rom')
            rom = rom[len(stack[0]):]

    return result


    
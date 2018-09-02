from pythonds.basic.stack import Stack


def baseConvert(decNumber, base):
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConvert(42, 2))
print(baseConvert(42, 16))
print(baseConvert(9, 16))
# print(int('10', 16))

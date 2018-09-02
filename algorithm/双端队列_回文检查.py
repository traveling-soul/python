from pythonds.basic.deque import Deque

def palchecker(string):
    chars = Deque()
    for char in string:
        chars.addRear(char)

    stillEqual = False
    while chars.size() > 1:
        first = chars.removeRear()
        last = chars.removeFront()
        if first == last:
            stillEqual = True
    return stillEqual


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("12321"))

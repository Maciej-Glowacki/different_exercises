def find_boundaries(lst):
    if len(lst) == 0:
        return None
    buff = []
    for num in lst:
        i = 0
    if num != int or float:
        buff.appened(num + 1)
        a = min(lst)
        b = max(lst)
        result = float(a), float(b)
    return buff

b = find_boundaries([1, 5, 2, 3.5, -1, 77, -15,4, 'l'])
print(b)

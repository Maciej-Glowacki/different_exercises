def find_first_and_last(lst):
    result = [lst[i] for i in (0, -1)]
    return tuple(result)

tple = find_first_and_last([9, 12, 44, 123])
print(tple)
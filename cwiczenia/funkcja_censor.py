def censor(data):
    words = ['Java', 'C#', 'Ruby', 'PHP']
    lst = list(data.split())

    for i in lst:
        for m in words:
            if i == m:
                idx = lst.index(i)
                lst[idx] = ('****')
    sep = (' ')
    s_tr = (sep.join(lst))
    return s_tr


c = censor("C# is the best, but PHP is the bestest!")
print (c)
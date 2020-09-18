def make_tuple(a, b, c = 3, d = 4):
    result = (a, b, c, d)
    return result

tpl = make_tuple("mama", "tata")
print(tpl)

tpl = make_tuple(22, "tata", 0, False)
print(tpl)
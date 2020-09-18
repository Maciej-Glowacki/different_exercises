title = 1
# title = 1.2
# title = '1'
# title = Exception
# if type(title) is int:
#     print('to jest int')
#     print(title * 5)
# else:
#     print('to NIE jest int')
#     if type(title) is float:
#         print('to jest float')
#         print(title / 5)
#     else:
#         print('to NIE jest float')
title = float(title)
if type(title) is int:
    print('to jest int')
    print(title * 5)
elif type(title) is float:
    print('to jest float')
    print(title / 5)
elif type(title) is str:
    print('to jest str')
    print(title)
else:
    print('to jest jakiś dziwny typ :) ')
def div(start, end):
    '''
    Func has to return list of numbers in list that can be divided by 2 and not by 3
    :param: list of numbers 
    :return nums from list that can be devided by 2 and not by 3
    '''
    return [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 != 0]


if __name__ == '__main__':

    print(div(1, 103))

def name_sorter(lst):
    '''Sorts names in dict for male and female names
    
    :param:list of names
    :return: dict with names separated
    '''
    
    result = {
        'female': [], 
        'male': [] 
        }
    for name in lst:
        if name[-1] == 'a':
            result['female'].append(name)
        else:
            result['male'].append(name)
    return result
            
if __name__ == '__main__':

    input_data = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]

    print(name_sorter(input_data))


names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))
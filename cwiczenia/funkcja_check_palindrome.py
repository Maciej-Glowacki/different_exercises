def check_palindrome(text):
    '''Checks if text is a palindrome

    :param: text
    :return: information True or False
    '''
    text = text.lower().replace(' ', '')
    return text == text[::-1]
    
    # if text == text[::-1]:
    #     return True
    # else:
    #     return False


if __name__ == '__main__':

    print(check_palindrome('kajak oko kajak'))

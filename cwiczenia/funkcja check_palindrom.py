def check_palindrome(data):
    if data == data[::-1]:
        return True
    else:
        return False

print(check_palindrome('kajak'))
import calendar
def format_date(day, month, year):
    if day not in range(1, 31):
        return None
    elif month == 2 and day not in range(1, 28):
        return None
    elif month not in range(1, 12):
        return None
    elif year not in range (0, 2021):
        return None

    months = {
        1: 'Styczeń',
        2: 'Luty',
        3: 'Marzec',
        4: 'Kwiecień',
        5: 'Maj',
        6: 'Czerwiec',
        7: 'Lipiec',
        8: 'Sierpień',
        9: 'Wrzesień',
        10: 'Październik',
        11: 'Listopad',
        12: 'Grudzień'
    }
    month = months[month]
    formatted_date = (f'{day} {month} {year}')
    return formatted_date

d = format_date(12, 1, 2017)
print(d)

d = format_date(12, 13, 2017)
print(d)
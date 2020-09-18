name = input('What is your name: ')
age = int(input('What is your age: '))
copies = int(input('How many copies of this sentence would you like to get? '))
present_year = 2020

how_many_years_to_100 = 100 - age
when_you_will_have_100 = present_year + how_many_years_to_100

print((f'{name}, You will have 100 years in {when_you_will_have_100} year \n') * copies)

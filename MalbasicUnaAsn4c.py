# Una Malbasic Assignment 4c

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

ins_date = input(str('Please enter the date in form: mm/dd/yyyy: '))

date = ins_date.split('/')

if not date[0].isnumeric():
       print('The format is invalid!')

elif len(date)<3:
    print('The date format is invalid!')
elif len(date[2])<4:
    print('The year format is invalid!')
elif date[0] < '01' or date[0] > '12':
        print('The month format is invalid!')

elif date[0] == '' or date[1] == '' or date[2] == '':
        print('The format is invalid!')

elif date[0] == '02' and date[1] >= '29':
        print(f'The format is invalid! The day entered is {date[1]}. This month cannot have more than 29 days!')

elif date[1] > '30' and (date[0] == '04' or date[0] =='06' or date[0] == '09' or date[0] == '11'):
        print(f'The format is invalid! The day entered is {date[1]}. This month cannot have more than 30 days')

elif date[1] > '31' and (date[0] == '01' or date[0] =='03' or date[0] == '05' or date[0] == '07' or date[0] == '08' or date[0] == '10' or date[0] == '12'):
        print(f'The format is invalid! The day entered is {date[1]}. This month cannot have more than 31 days')

else:
        month = int(date[0]) -1
        print(f'{Months[month]} {date[1]}, {date[2]}')
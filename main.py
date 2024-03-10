year = int(input('Enter the year : '))
# a = True
# b = True
# c = True
# if year % 4 == 0:
#     a = True
# else:
#     a = False
# if year % 100 == 0:
#     b = False
# else:
#     b = True
# if year % 400 == 0:
#     c = True
# else:
#     c = False
#
# if a and b:
#     print('This is leap year')
# elif a and c:
#     print('This leap year')
# elif b and c:
#     print('This is leap year')
# else:
#     print('This is not a leap year')
#
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not Leap year')
    else:
        print('Leap year')
else:
    print('Not Leap Year')
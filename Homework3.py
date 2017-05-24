
# def distance(x1,y1,x2,y2):
#     result = (x1 - y1)**0.5 + (x2 - y2)**0.5
#     return result
# x1 = float(input('Enter: '))
# y1 = float(input('Enter: '))
# x2 = float(input('Enter: '))
# y2 = float(input('Enter: '))
# print(distance(x1,y1,x2,y2))

# def is_year_leap(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('True')
#     else:
#         print('False')
# is_year_leap(2)

def function(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("True")
    else:
        print("False")
function(0,2,15)

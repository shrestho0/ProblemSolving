


# def check_leap_year(y):
#     if y % 100 == 0:
#         if y % 400 != 0:
#             return "No"
#         else:
#             return "Yes"
#     else:
#         if y % 4 == 0:
#             return "Yes"
#         else:
#             return "No"


# print(check_leap_year(int(input())))
# print(check_leap_year(2018))
# print(check_leap_year(2012))
# print(check_leap_year(1900))
# print(check_leap_year(2100))


# import calendar
# print("Yes") if calendar.isleap(int(input())) else print("No")

# y = int
# print("Yes") if 0 < y < 9999 and y%4 ==0 and y%400 != 0 else print("No")


y = int(input())
print("Yes") if y%4==0 and y%400!=0 else print("No")
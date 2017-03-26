from enum import Enum, unique
#
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

Week = Enum('Week', ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))

for name, month in Month._member_map_.items():
    print(name, ' --> ', month)
for name in Month._member_names_:
    print(name)
for month in Month:
    print(month.value, ' -- ', month)

for name, weekday in Week._member_map_.items():
    print(weekday.value, ' -- ', name)


@unique
class Weekday(Enum):
    Sun, Mon, Tue, Wed, Thu, Fri, Sat = 0, 1, 2, 3, 4, 5, 6

print(Weekday.Sun.value)
print(Weekday.Fri.name)
print(Weekday(3))

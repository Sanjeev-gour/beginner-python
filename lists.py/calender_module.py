import calendar
"""

#to print the calendar of specific month
cal = calendar.month(2016,1)

print(cal)

# check the leap year
print(calendar.isleap(2016))

print(calendar.isleap(2015))
"""

#imported the module made by e
import Own_module as om

area = om.calculate_area_square(5)
print(area)

#if the module is not present in the same directory 
#then import sys module 
#sys.path.append("path of module")
#import module


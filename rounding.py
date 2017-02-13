x = 27.68

#ENTER CODE BELOW HERE
s_x = str(x)
_dian = s_x.find('.')
if int(s_x[_dian + 1]) >=5:
    print (int(s_x[:_dian]) + 1)
else:
    print (int(s_x[:_dian]))

speed_of_light = 300000. # km per second

def speed_fraction(tracert, distance):
    return distance * 2 / tracert * 1000 / speed_of_light

print (speed_fraction(16,20))

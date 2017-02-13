def convert_seconds(sec):
    hour = int(sec / 3600)
    minute = int((sec % 3600)/60)
    second = sec % 3600 % 60
    if hour <= 1:
        if minute == 1 and second == 1:
            return "%d hour, %d minute, %d second" % (hour, minute, second)
        if minute == 1 and second != 1:
            return "%d hour, %d minute, %.1f seconds" % (hour, minute, second)
        if minute != 1 and second == 1:
            return "%d hour, %d minutes, %d second" % (hour, minute, second)
        else:
            return "%d hour, %d minutes, %.1f seconds" % (hour, minute, second)
    if hour > 1:
        if minute == 1 and second == 1:
            return "%d hours, %d minute, %d second" % (hour, minute, second)
        if minute == 1 and second != 1:
            return "%d hours, %d minute, %.1f seconds" % (hour, minute, second)
        if minute != 1 and second == 1:
            return "%d hours, %d minutes, %d second" % (hour, minute, second)
        else:
            return "%d hours, %d minutes, %.1f seconds" % (hour, minute, second)
    return hour, minute, second


# print (convert_seconds(40960))
# # >>> 1 hour, 1 minute, 1 second
#
# print (convert_seconds(7325))
# # >>> 2 hours, 2 minutes, 5 seconds
#
# print (convert_seconds(7261.7))
# # >>> 2 hours, 1 minute, 1.7 seconds
#
# print (convert_seconds(623))


def download_time(size, size_item, speed, speed_item):
    return convert_seconds((size / speed) * unit_trans(size_item, speed_item))

def unit_trans(p_unit, q_unit):
    if p_unit == q_unit:
        return 1
    #The pakage's unit is kB
    if p_unit == 'kB':
        if q_unit == "kb":
            return 8
        if q_unit == "MB":
            return 1/1024
        if q_unit == "GB":
            return (1/1024) ** 2
        if q_unit == "Mb":
            return 8/1024
        else:
            return (1/1024)*(1/1024)*8
    #The pakage's unit is MB
    if p_unit == "MB":
        if q_unit == "kb":
            return 8 * 1024
        if q_unit == "kB":
            return 1024
        if q_unit == "GB":
            return 1/1024
        if q_unit == "Mb":
            return 8
        else:
            return 8/1024
    # The pakage's unit is GB
    if p_unit == "GB":
        if q_unit == "Gb":
            return 8
        if q_unit == "MB":
            return 1024
        if q_unit == "Mb":
            return 8 * 1024
        if q_unit == "kb":
            return 8 * 1024 * 1024
        else:
            return 1024 ** 2

print (download_time(1024,'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print (download_time(1024,'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print (download_time(13,'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print (download_time(13,'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print (download_time(10,'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print (download_time(10,'MB', 2, 'kb'))
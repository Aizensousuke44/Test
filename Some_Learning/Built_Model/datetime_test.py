import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, zt_str):
    dt_stamp = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    match = re.match(r'^UTC(\+|-)(0[0-9]|[0-9]):00$', zt_str)
    zone = int(match.group(2))
    dt = dt_stamp.astimezone(timezone(timedelta(hours=zone)))

    return dt.timestamp()

if __name__ == '__main__':
    t1 = to_timestamp('2017-09-12 09:17:44', 'UTC+3:00')
    print(t1)
    t2 = to_timestamp('2016-1-3 14:24:54', 'UTC-09:00')
    print(t2)
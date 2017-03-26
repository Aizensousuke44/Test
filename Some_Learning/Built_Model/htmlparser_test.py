import re
from collections import namedtuple
from contextlib import closing
from urllib.request import urlopen

from bs4 import BeautifulSoup

info = []
Event = namedtuple('Event', ['title', 'time', 'address'])

with closing(urlopen('https://www.python.org/events/python-events/')) as py:
    soup = BeautifulSoup(py, 'html.parser')

    title_list = soup.find_all('h3', class_=re.compile(r'^event-title$'))
    time_list = soup.find_all('time')
    addr_list = soup.find_all('span', class_=re.compile(r'^event-location$'))

    for title, tm, addr in zip(title_list, time_list, addr_list):
        event = Event(title.get_text(), tm.get_text(), addr.get_text())
        info.append(event)

for item in info:
    print(item)
import re

string = 'Jack is the king of 365 kingdoms'

# search is same as match
tag = re.search(r'\d+', string)
print(tag)
print(tag.group())

# findall() return a list
tag = re.findall(r'[\D]+', string)
print(tag)

# sub -- replace, return a string
tag = re.sub(r'\s', '_', string)
print(tag)

# split, return a list
tag = re.split(r'i', string)
print(tag)

num_str = 'asf435fahgth86faesg13asdg09876vdrst'
tag = re.split(r'\d+', num_str)
print(tag)
tag = [i for i in re.split(r'\D+', num_str) if i != '']
print(tag)
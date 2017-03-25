import re

# match return a addr,
# if it matched, the matched content in group()
def match_test(rule, content):
    try:
        tag = re.match(rule, content)
        print(tag.group())
    except:
        print('Not match')


if __name__ == '__main__':
    rule = r'[A-Z][a-z]*'
    content = 'Aizensousuke'
    match_test(rule, content)

    rule = r'[A-Z][a-z]*\d*'
    content = 'Aizensousuke724'
    match_test(rule, content)

    rule = r'[_A-Za-z0-9]{6,16}@(gmail|outlook|qq|163|yahoo).(com|cn)$'
    content = 'aizensousuke724@yahoo.org'
    match_test(rule, content)
    # \A, \Z
    rule = r'\A[A-Z][a-z]*\d\Z'
    content = 'Aizen44'
    match_test(rule, content)

    # (rules) create a group
    # \num call the numth group
    # (?P<name>[rules]) create and named a group
    # (?P=name) call the named group
    rule = r'<(?P<title>[\w]+>)[ _\w]+</(?P=title)'
    content = '<p>Hello world</p>'
    match_test(rule, content)
    rule = r'<([\w]+>)[ _\w]+</\1'
    match_test(rule, content)

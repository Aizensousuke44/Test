def reverse(text):
    rev = ''
    count = len(text)
    while count > 0:
        rev += text[count - 1]
        count -= 1
    return rev
   

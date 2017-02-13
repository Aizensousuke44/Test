def is_palindrome_first(content):
    if isinstance(content, int):
        content = str(content)
    if content == '' or len(content) == 1:
        return True
    if content[0] == content[-1]:
        return is_palindrome_first(content[1:-1])
    else:
        return False

def is_palindrome_second(content):
    if isinstance(content, int):
        content = str(content)
    if content == '' or len(content) == 1:
        return True
    if content == content[::-1]:
        return True
    else:
        return False

def is_palindrome_iter(content):
    if isinstance(content, int):
        content = str(content)
    if content == '' or len(content) == 1:
        return True
    for i in range(0, len(content) // 2):
        if content[i] != content[-(i + 1)]:
            return False
    return True

print(is_palindrome_first(3456543))
print(is_palindrome_second(3456543))
print(is_palindrome_iter(3456543))
print(is_palindrome_iter(345543))
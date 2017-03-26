import base64

def safe_base64_decode(string):
    string += (b'=' * (len(string)%4))
    return base64.b64decode(string)

if __name__ == '__main__':
    print(base64.b64decode('HKJAGSiO=='))

    assert b'\x1c\xa2@\x19(\x8e' == safe_base64_decode(b'HKJAGSiO=='), safe_base64_decode(b'HKJAGSiO==')


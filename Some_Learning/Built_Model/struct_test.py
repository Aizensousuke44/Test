import struct

# get file.bmp's information
def check_bmp(file_name):

    with open(file_name, 'rb') as bp:
        file = bp.read()
        fl = struct.unpack('asfjief<>/aefg', file[:30])
        for i in fl:
            print(i, ' ')
        if (fl[0] == b'B') & (fl[1] == b'M'):
            print()
            print('It is BMP file \nhigh: %s, weight: %s,\nThe Colornumbers: %s' % (fl[6], fl[7], fl[9]))

if __name__ == '__main__':
    pass
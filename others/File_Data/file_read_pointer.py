import os

with open('file_test.html') as file:
    # readline() for first line,
    # return a string
    print(file.readline())
    print(file.tell())
    # move the pointer to the beginning
    file.seek(0, os.SEEK_SET)
    # readlines() for all
    # return a list
    print([i.strip() for i in file.readlines()])
    print(file.tell())
    file.seek(0, os.SEEK_SET)
    # read() return all things with format
    # return a string
    print('Thing: %s \nThe type is %s' % (file.read(), type(file.read())))

    # move pointer to the end
    print(file.seek(0, os.SEEK_END), file.tell())
    # move pointer to somewhere we want
    print(file.seek(7, os.SEEK_SET), file.tell())


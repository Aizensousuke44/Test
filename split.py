def split_string(source, splitlist):
    output = []
    flagsplit = True

    for char in source:
        if char in splitlist:
            flagsplit = True
        else:
            if flagsplit:
                output.append(char)
                flagsplit = False
            else:
                output[-1] = output[-1] + char
    return output

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print (out)

out = split_string("After  the flood   ...  all the colors came out.", " .")
print (out)

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print (out)
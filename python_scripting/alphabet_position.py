def alphabet_position(text):
    position = ""
    for x in text:
        num = ord(x)
        if 64 < num < 90:
            position += str(num-64) + " "
        if 96 < num < 122:
            position += str(num-96) + " "
    print(position)


alphabet_position("The sunset sets at twelve o' clock.")
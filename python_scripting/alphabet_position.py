def alphabet_position(text):
    position = ""
    for x in text:
        num = ord(x)
        if 64 < num < 91:
            position += str(num-64) + " "
        if 96 < num < 123:
            position += str(num-96) + " "
    return position[:-1]


print(alphabet_position("The sunset sets at twelve o' clockZz."))

def unique_in_order(sequence):
    # my_array = list(sequence)
    # print(len(sequence))
    a = ''
    my_array=[]
    for i in sequence:
        if i != a:
            my_array.append(i)
            a = i
    return my_array

print(unique_in_order("AABBCDC"))
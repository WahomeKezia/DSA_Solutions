def occur_string(some_string):
    arr_char = list(some_string)
    counter = 0
    for val in arr_char:
        if val=='k'or val=='K':
            counter += 1
    return counter


result1 = occur_string('Kangaroo')
result2 = occur_string('something')
print(result1)
print( result2)







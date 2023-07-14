with open('land.txt','r') as file:
"""
    data = file.read()
    lines = file.readlines()
    second_line = data[0].split(" ")
    item = int(second_line[0])
    print(item)

"""
    for string in file:
        string_list = string.split()
        for symbol in string_list:
            print(int(symbol)+ 1)
#            print(int(symbol)+1)

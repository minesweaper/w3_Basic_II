def string_to_list(string):
    new_list = string.split(" ")
    return new_list


x = "A new string that will be split to a list"
print(string_to_list(x))
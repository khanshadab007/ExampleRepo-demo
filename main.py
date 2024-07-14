#This is an example code
print("Linear Search Function")


def linear_search(input_list, element):
    for index, value in enumerate(input_list):
        if value == element:
            return index

    return -1


uinput_list = [3, 4, 1, 6, 14]
uelement = 4
print("Index position for the element x is:", linear_search(uinput_list, uelement))

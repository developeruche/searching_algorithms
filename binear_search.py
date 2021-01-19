""" This is a more efficent way of sorting data, when it come to timing and computational power this
algorithm stands out but there is a catch this algorithm only work for sorted data(array) """

def binary_search(element, array):
    starting_index = 0
    mid_index = 0
    last_index = len(array) - 1

    while starting_index <= last_index:
        mid_index = (starting_index + last_index) // 2
        current_mid_element = array[mid_index]

        if current_mid_element == element:
            return mid_index

        if current_mid_element < element:
            starting_index = mid_index + 1
        else:
            last_index = mid_index + 1
        
    return -1


""" This is a algorithm that would conduct a linear search on a data """

def linear_search(element, array):
    for index_i, element_i in array:
        if element_i == element:
            return index_i
        else:
            return -1

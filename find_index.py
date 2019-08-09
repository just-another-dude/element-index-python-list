# Standard Library Modules
import sys


def find_index(list):
    """
    :param list: Receive a list of integers (numbers).
    :return: An element index for which the sum of all values in the list up to and including that index is equal
     to the sum of all values in the list from the position after that index until the end of the list.
    """

    sum_of_list = sum(list)  # The total sum of all of the elements in the list.
    half_of_sum = int(sum_of_list / 2)  # Half of the total sum.
    increment_sum = 0  # Variable for storing incrementally rising sum in the following for loop.
    element_index = None  # The element index in the list where the sum will be half.

    for num in list:
        increment_sum += num
        if int(increment_sum) == half_of_sum:
            element_index = list.index(num)
            break

    if element_index == None:
        sys.exit("An element index with the necessary requirements HAS NOT been found!")

    return element_index


def main():
    # Variable
    num_list = [1, 2, 3, 6]

    # Script
    list_index = find_index(num_list)
    print("The element index is: {}".format(list_index))


if __name__ == '__main__':
    main()

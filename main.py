# Created by:   Patrick Archer
# Date:         20 December 2018
# Copyright to the above author. All rights reserved.

"""

Directions - COMPLETE:
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras - INCOMPLETE:
(1 - COMPLETE) Randomly generate two lists to test this
(2 - INCOMPLETE) Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""

import random

# ################################################# start_funcs

# check lists
def checkLists(list1, list2):

    # instantiate initial results list
    list3 = []

    # parse both passed lists by each respective element and compare their values
    for n1 in range(len(list1)):
        for n2 in range(len(list2)):
            # if element value equivalent within both lists
            if (list1[n1] == list2[n2]):
                # if element value doesn't already exist in the results list
                if (not list1[n1] in list3):
                    # append element value to results list
                    list3.append(list1[n1])

    # return results list (contains all values present in both list1 and list2)
    return list3

# ################################################# end_funcs/start_main

# generate 1st list array of randomly generated size w/ randomly generated element int values
random_list1 = []
for r1 in range(random.randrange(5, 50, 5, int)):
    random_list1.append(random.randrange(1, 100, 1, int))

# print 1st randomly-generated list
print("\nRandom List #1:")
print(random_list1)

# generate 2nd list array of randomly generated size w/ randomly generated element int values
random_list2 = []
for r2 in range(random.randrange(5, 50, 5, int)):
    random_list2.append(random.randrange(1, 100, 1, int))

# print 2nd randomly-generated list
print("\nRandom List #2:")
print(random_list2)

# call compare func, store return in resultingSimilarities array/list
resultingSimilarities = checkLists(random_list1, random_list2)

# print result
print("\nNumbers that were contained in both randomly-generated lists:\n" + str(resultingSimilarities))

# ################################################# end_main







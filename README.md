# General
This is an excercise where one puts their programming skills to the test. It can be used for any programming language, however here it is explained and solved in English & Python 3 ;).
Note that this excercise should not take more than 20-25 minutes to finish by yourself.


# Characterizing the excercise
Write a function that receives a list filled with numbers (integers). The function should return an index in the list for which the sum of all values in the list up to and including that index is equal to the sum of all values in the list from the position after that index until the end of the list.


# Solution Workflow
* Calculate the overall sum of the inputted list.
* Determine half of the sum value by dividing it by 2.
* Run a for loop on the list elements and add them incrementally to a variable up until it reaches half of the overall sum or until all elements are added.
* If the variable stated above reaches half of the overall sum at some point, then the element that was added last would be the element we are looking for, therefore we break out of the loop and return that elements' index.
* If the variable stated above DOES NOT reach half of the overall sum and the for loop finishes its run, then an element with the necessary requirements doesn't exist.

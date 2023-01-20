# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

    # "flatten an array" means to "reduce the demensionality of an array"
    #  example: my_array = [[1,2], 3, 4, 5, [6,7]]
            # result of "flattened" array:
            # flattened_array = [1,2,3,4,5,6,7]

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?
    # The original array does not change when this function is instanciated.
    # A new array(list) is created on line 9.
    

Is this solution a pure function? Why or why not?
    # yes.  the values sent in are not changed. 

Is this solution a higher order function? Why or why not?
    # yes.  The line 13 returns a built-in method(function).

Would it have been easier to solve this problem using a different programming style?
    # maybe. I do not know enough to know.

Why in particular is functional programming a helpful paradigm when solving this problem?
    # code for this particular problem does not require many steps to solve.
'''

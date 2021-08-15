# Problem Set 4A
# Name: gcnTo
# Collaborators: None
# Time Spent: 5-7 hours thinking + 10-30 minutes implementing

import time
import copy 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    #PSEUDO CODE
    #IF THERE ARE MORE THAN TWO ITEMS LEFT
        #IF THERE'S A LIST ITEM
            #INSERT NON LIST ITEM TO LIST ITEM
            #RETURN INSERTED LIST
        #IF THERE'S NO LIST ITEM
            #SPLIT
    #IF THERE ARE TWO ITEMS LEFT
        #PERMUTE
        #RETURN PERMUTED LIST
    

    if type(sequence) == str:
        if len(sequence) == 1:
            return sequence
        return get_permutations([sequence[:1],get_permutations(sequence[1:])])
    elif type(sequence) == list:
            insert_range = len(sequence[1][0]) + 1
            temp_list = []
            for permuted in sequence[1]:
                for i in range(insert_range):
                    temp = permuted[:i] + sequence[0] + permuted[i:]
                    temp_list.append(temp)
            return temp_list
    
        
            
        
          
            

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input_1 = "ab"
    print("Input:", example_input_1)
    print("Expected Output:", ['ab','ba'])
    print("Actual Output:", get_permutations(example_input_1))
    if set(['ab','ba']) == set(get_permutations(example_input_1)):
        print("Correct.","\n")

    example_input_2 = "abc"
    print("Input:", example_input_2)
    print("Expected Output:", ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print("Actual Output:", get_permutations(example_input_2))
    if set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == set(get_permutations(example_input_2)):
        print("Correct.","\n")

    example_input_3 = "123"
    print("Input:", example_input_3)
    print("Expected Output:", ['123', '132', '213', '231', '312', '321'])
    print("Actual Output:", get_permutations(example_input_3))
    if set(['123', '132', '213', '231', '312', '321']) == set(get_permutations(example_input_3)):
        print("Correct.")


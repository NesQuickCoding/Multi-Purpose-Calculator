# -*- coding: utf-8 -*-
"""
# Class work 6
# Create adjacency list
"""

import pprint

      
    
    
# Know if it's one way or two way direction    
# if the input is (1,4) and you are expect 1 -> 4
# vs if it means that 4 -> 1
# if it means that 1 -> 4 and 4 -> 1

#
# Packs and unpacks
# start args packs the argument 
# (*args) gives multiple arguments
#make_adjacency_list((1,2), (1,3), (2,1), (2,4))


# Keyword Args = kwargs
# if you input star star kwargs
# thats keyword args (kword args)
# (**kwargs)
#make_adjacency_list((1,2), (1,3), (2,1), (2,4), 'abc', key = '123', key2 = 'my heart')

# This helps you see the doc
#print(make_adjacency_list.__doc__)

# Implicit error example
#test_case = make_adjacency_list([])


def count_nodes(*args):
    
    # Sets cost more to maintain than list 
    # Because they have a way of knowing if a value exist or not
    set_of_nodes = set()
    for edge_pair in args:
        set_of_nodes.add(edge_pair[0])
        set_of_nodes.add(edge_pair[1])
        
    return set_of_nodes, len(set_of_nodes)

count_test_1 = count_nodes((1,2), (1,3), (2,1), (2,4),
                           (3,1), (3,4), (4,2), (4,3), (4,5), (5,4))


#print(count_test_1)


def make_adjacency_matrix(*args):
    # Only the first value 
    count = count_nodes(*args)[1]
    adjacency_matrix = []
    
    list_to_append = []
    
    for value in range(count + 1):
        list_to_append.append(0)
    
    # To help with the count by 1 error
    for value in range(count + 1):
        adjacency_matrix.append(list_to_append)
        
    print(count)
    pprint(adjacency_matrix)
    
    

# Here is your assignment

# Remember those cases from earlier? Now you have to do that

# Give me code from an adhacency list and matrix for both of those cases
# Specifically functions

# (1,4) 4 -> 1 and also the case of 1->4 and 4->1

# Write up those functions into a class for lists
# And a class for matrices


# Besides creating a list and matrix, 
# they should also do things like give me an
# Edgelist
# Count of all Nodes
class matrix:
    def __init__(self, *args):
        for i in args:
            print(i)
        pass
    
    def count_nodes(self, *args):    
        set_of_nodes = set()
        for edge_pair in args:
            set_of_nodes.add(edge_pair[0])
            set_of_nodes.add(edge_pair[1])
        return set_of_nodes, len(set_of_nodes)
        
        
class adjacency_list:
    def __init__(self, *args):
        
        pass
    
#print(node(1,2))
ans = count_nodes((1,2), (1,3), (2,1), (2,4),
                           (3,1), (3,4), (4,2), (4,3), (4,5), (5,4))
        
print(ans)
        

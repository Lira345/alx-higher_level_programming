#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuple_a has at least 2 elements, filling with zeros if necessary
    tuple_a += (0, 0)
    # Ensure tuple_b has at least 2 elements, filling with zeros if necessary
    tuple_b += (0, 0)
    
    # Sum the first two elements of each tuple and return as a new tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

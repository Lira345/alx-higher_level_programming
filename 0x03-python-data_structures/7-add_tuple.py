def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuple_a has at least 2 elements by filling with zeros if necessary, then take the first 2 elements
    tuple_a = (tuple_a + (0, 0))[:2]
    # Ensure tuple_b has at least 2 elements by filling with zeros if necessary, then take the first 2 elements
    tuple_b = (tuple_b + (0, 0))[:2]

    # Sum the first two elements of each tuple and return as a new tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])                

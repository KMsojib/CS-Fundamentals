def main():
    # Creating a tuple
    my_tuple = (1, 2, 3, 4, 5)
    
    # Accessing elements in a tuple
    print("First element:", my_tuple[0])
    print("Last element:", my_tuple[-1])
    
    # Slicing a tuple
    print("Slice from index 1 to 3:", my_tuple[1:4])
    
    # Tuple unpacking
    a, b, c, d, e = my_tuple
    print("Unpacked values:", a, b, c, d, e)
    
    # Nested tuples
    nested_tuple = (1, (2, 3), (4, 5))
    print("Nested tuple:", nested_tuple)
    
    # Tuple methods
    print("Count of 2 in tuple:", my_tuple.count(2))
    print("Index of 3 in tuple:", my_tuple.index(3))
    
    # Allow Duplicates
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(thistuple)
    
    # join tuple
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)
    tuple3 = tuple1 + tuple2
    print("Joined tuple:", tuple3)
    
    

if name == "__main__":
    main()
   
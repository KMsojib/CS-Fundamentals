def main():
    # Create a set
    my_set = {1, 2, 3, 4, 5}
    print("Original set:", my_set)

    # Add an element to the set
    my_set.add(6)
    print("Set after adding an element:", my_set)

    # Remove an element from the set
    my_set.remove(3)
    print("Set after removing an element:", my_set)

    # Check if an element is in the set
    print("Is 4 in the set?", 4 in my_set)

    # Iterate through the set
    print("Iterating through the set:")
    for item in my_set:
        print(item)
    
    # set methods
    my_set = {1, 2, 3, 4, 5}
    # union
    another_set = {4, 5, 6, 7}
    union_set = my_set.union(another_set)
    print("Union of sets:", union_set)
    
    # intersection
    intersection_set = my_set.intersection(another_set)
    print("Intersection of sets:", intersection_set)
    # difference
    difference_set = my_set.difference(another_set)
    print("Difference of sets:", difference_set)
    

if name == "__main__":
    main()
   
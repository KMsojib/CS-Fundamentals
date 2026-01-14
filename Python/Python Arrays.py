array = """
Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
"""

def main():
    # Array of integers
    arr = [1, 2, 3, 4, 5]
    # Print the array
    print("Array of integers:", arr)
    
    
    # Array methods
    # Append an element
    arr.append(6)
    print("After appending 6:", arr)
    
    # Insert an element at index 2
    arr.insert(2, 10)
    print("After inserting 10 at index 2:", arr)
    
    # Remove an element
    arr.remove(10)
    print("After removing 10:", arr)
    
    # Pop an element
    popped_element = arr.pop()
    print("Popped element:", popped_element)
    
    # Sort the array
    arr.sort()
    print("Sorted array:", arr)
    
    # Reverse the array
    arr.reverse()
    print("Reversed array:", arr)
    
    # Array slicing
    sliced_array = arr[1:4]
    print("Sliced array (index 1 to 4):", sliced_array)
    
    # Array length
    array_length = len(arr)
    print("Length of array:", array_length)
    
    # Array concatenation
    arr2 = [7, 8, 9]
    concatenated_array = arr + arr2
    print("Concatenated array:", concatenated_array)
    
if __name__ == "__main__":
    main()
    



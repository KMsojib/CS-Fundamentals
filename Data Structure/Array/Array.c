/*
Array Lesson for Junior Students (C Language)
---------------------------------------------

What is an Array?
-----------------
An array is a collection of variables of the same type, stored in contiguous memory locations. 
Arrays allow you to store multiple values together and access them using indices.

Why use Arrays?
---------------
- To store multiple items of the same type.
- To process data efficiently.

Declaring Arrays
----------------
Syntax:
datatype arrayName[arraySize];

Example:
*/
#include <stdio.h>

int main() {
    // Integer array with 5 elements
    int numbers[5] = {1, 2, 3, 4, 5};
    printf("Numbers array: ");
    for(int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    // Array of strings (array of character arrays)
    char fruits[3][10] = {"apple", "banana", "cherry"};
    printf("Fruits array: ");
    for(int i = 0; i < 3; i++) {
        printf("%s ", fruits[i]);
    }
    printf("\n");

    // Accessing Array Elements
    printf("First number: %d\n", numbers[0]); // Output: 1
    printf("Second fruit: %s\n", fruits[1]);  // Output: banana

    // Changing Array Elements
    numbers[2] = 10;
    printf("Changed numbers array: ");
    for(int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    // Getting Array Size (for statically allocated arrays)
    printf("Length of numbers array: %lu\n", sizeof(numbers)/sizeof(numbers[0]));

    // Looping Through Arrays
    printf("Looping through fruits: ");
    for(int i = 0; i < 3; i++) {
        printf("%s ", fruits[i]);
    }
    printf("\n");

    // Practice Exercises
    // 1. Create an array of your three favorite colors and print it.
    char colors[3][10] = {"red", "blue", "green"};
    printf("Favorite colors: ");
    for(int i = 0; i < 3; i++) {
        printf("%s ", colors[i]);
    }
    printf("\n");

    // 2. Change the second color to "yellow" and print the array.
    // Note: To change the string, use strcpy from <string.h>
    #include <string.h>
    strcpy(colors[1], "yellow");
    printf("Changed colors: ");
    for(int i = 0; i < 3; i++) {
        printf("%s ", colors[i]);
    }
    printf("\n");

    // 3. Print each color using a loop.
    printf("Printing colors (one by one):\n");
    for(int i = 0; i < 3; i++) {
        printf("%s\n", colors[i]);
    }

    // Common Array Mistakes
    // - Indexing starts at 0, not 1!
    // - Accessing an index out of range causes undefined behavior.

    // Uncommenting the next line may cause an error!
    // printf("%d\n", numbers[10]); // Out of range!

    return 0;
}

/*
Extra: Arrays in C
------------------
- Arrays have fixed size (size must be known at compile time).
- All elements must be of the same type.
- For dynamic arrays, use malloc/free (advanced topic).

References
----------
- https://www.programiz.com/c-programming/arrays
- https://www.w3schools.com/c/c_arrays.php

End of Lesson
*/
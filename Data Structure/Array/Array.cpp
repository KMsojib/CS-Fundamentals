/*
Array Lesson for Junior Students (C++)
--------------------------------------

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
#include <iostream>
using namespace std;

int main() {
    // Integer array with 5 elements
    int numbers[5] = {1, 2, 3, 4, 5};
    cout << "Numbers array: ";
    for(int i = 0; i < 5; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;

    // Array of strings (C++11 and later)
    string fruits[3] = {"apple", "banana", "cherry"};
    cout << "Fruits array: ";
    for(int i = 0; i < 3; i++) {
        cout << fruits[i] << " ";
    }
    cout << endl;

    // Accessing Array Elements
    cout << "First number: " << numbers[0] << endl; // Output: 1
    cout << "Second fruit: " << fruits[1] << endl;  // Output: banana

    // Changing Array Elements
    numbers[2] = 10;
    cout << "Changed numbers array: ";
    for(int i = 0; i < 5; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;

    // Getting Array Size (for statically allocated arrays)
    cout << "Length of numbers array: " << sizeof(numbers)/sizeof(numbers[0]) << endl;

    // Looping Through Arrays
    cout << "Looping through fruits: ";
    for(int i = 0; i < 3; i++) {
        cout << fruits[i] << " ";
    }
    cout << endl;

    // Practice Exercises
    // 1. Create an array of your three favorite colors and print it.
    string colors[3] = {"red", "blue", "green"};
    cout << "Favorite colors: ";
    for(int i = 0; i < 3; i++) {
        cout << colors[i] << " ";
    }
    cout << endl;

    // 2. Change the second color to "yellow" and print the array.
    colors[1] = "yellow";
    cout << "Changed colors: ";
    for(int i = 0; i < 3; i++) {
        cout << colors[i] << " ";
    }
    cout << endl;

    // 3. Print each color using a loop.
    cout << "Printing colors (one by one):" << endl;
    for(int i = 0; i < 3; i++) {
        cout << colors[i] << endl;
    }

    // Common Array Mistakes
    // - Indexing starts at 0, not 1!
    // - Accessing an index out of range causes undefined behavior.

    // Uncommenting the next line may cause an error!
    // cout << numbers[10] << endl; // Out of range!

    return 0;
}

/*
Extra: Arrays in C++
--------------------
- Arrays have fixed size (size must be known at compile time).
- All elements must be of the same type.
- C++ also supports dynamic arrays using vectors (see <vector> library).

References
----------
- https://www.programiz.com/cpp-programming/arrays
- https://www.w3schools.com/cpp/cpp_arrays.asp

End of Lesson
*/
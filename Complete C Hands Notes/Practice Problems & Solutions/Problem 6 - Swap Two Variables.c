/*
Problem Statement: Swap the values of two variables using a temporary variable.

Explanation: Use a third variable to hold one value during the swap.

Solution:
*/
#include <stdio.h>

int main() {
    int a = 5, b = 10, temp;
    temp = a;
    a = b;
    b = temp;

    printf("a = %d, b = %d\n", a, b);
    return 0;
}

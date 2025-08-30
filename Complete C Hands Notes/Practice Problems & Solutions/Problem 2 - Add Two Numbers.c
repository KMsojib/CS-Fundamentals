// Problem Statement: Take two integers as input and print their sum.

// Explanation: Use scanf() to take input and printf() to display the result.

// Solution:
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("Sum = %d\n", a + b);
    return 0;
}

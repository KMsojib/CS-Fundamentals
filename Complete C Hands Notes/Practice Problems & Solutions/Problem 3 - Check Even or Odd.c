/*
Problem Statement: Input a number and print whether it is even or odd.

Explanation: Use % operator to check divisibility by 2.

Solution:
*/
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (num % 2 == 0)
        printf("Even\n");
    else
        printf("Odd\n");

    return 0;
}

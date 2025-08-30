/*
Problem Statement: Input a number and print its reverse (e.g., 123 → 321).

Explanation: Extract digits using % and build the reversed number.

Solution:
*/

#include <stdio.h>

int main() {
    int num, reverse = 0;
    printf("Enter a number: ");
    scanf("%d", &num);

    while (num != 0) {
        reverse = reverse * 10 + num % 10;
        num /= 10;
    }

    printf("Reversed number: %d\n", reverse);
    return 0;
}

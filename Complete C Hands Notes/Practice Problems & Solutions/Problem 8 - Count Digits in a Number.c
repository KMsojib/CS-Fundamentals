/*
Problem Statement: Input a number and count how many digits it has.

Explanation: Divide the number by 10 repeatedly until it becomes 0.

Solution:
*/
#include <stdio.h>

int main() {
    int num, count = 0;
    printf("Enter a number: ");
    scanf("%d", &num);

    while (num != 0) {
        num /= 10;
        count++;
    }

    printf("Number of digits: %d\n", count);
    return 0;
}

/*
Problem Statement: Input a number and print its multiplication table up to 10.

Explanation: Use a for loop to iterate from 1 to 10.

Solution:
*/
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", num, i, num * i);
    }

    return 0;
}

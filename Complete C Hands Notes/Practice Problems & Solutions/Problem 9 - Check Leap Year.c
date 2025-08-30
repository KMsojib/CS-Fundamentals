/*
Problem Statement: Input a year and check if it’s a leap year.

Explanation: Leap year rules: divisible by 4 but not 100, unless divisible by 400.

Solution:
*/

#include <stdio.h>

int main() {
    int year;
    printf("Enter a year: ");
    scanf("%d", &year);

    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
        printf("Leap year\n");
    else
        printf("Not a leap year\n");

    return 0;
}

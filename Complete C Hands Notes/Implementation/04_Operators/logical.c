#include <stdio.h>

int main() {
    int a = 1; // true
    int b = 0; // false

    printf("a && b = %d\n", a && b); // AND
    printf("a || b = %d\n", a || b); // OR
    printf("!a = %d\n", !a);         // NOT

    return 0;
}

#include <stdio.h>

int main() {
    int x = 12345;
    float y = 12.34567;

    printf("Default integer: %d\n", x);
    printf("Integer with width: %8d\n", x); // spaces before number
    printf("Float with 2 decimals: %.2f\n", y);
    printf("Float with 4 decimals: %.4f\n", y);

    return 0;
}

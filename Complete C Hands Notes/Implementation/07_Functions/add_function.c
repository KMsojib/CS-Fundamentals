#include <stdio.h>

// Function definition
int add(int x, int y) {
    return x + y;
}

int main() {
    int a = 5, b = 7;
    int result = add(a, b);

    printf("Sum = %d\n", result);
    return 0;
}

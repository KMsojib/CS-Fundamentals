/*
Problem Statement: Input two numbers and an operator (+, -, *, /) and perform the calculation.

Explanation: Use switch to handle different operations.

Solution:
*/
#include <stdio.h>

int main() {
    float a, b;
    char op;
    printf("Enter expression (e.g. 5 + 3): ");
    scanf("%f %c %f", &a, &op, &b);

    switch (op) {
        case '+': printf("Result = %.2f\n", a + b); break;
        case '-': printf("Result = %.2f\n", a - b); break;
        case '*': printf("Result = %.2f\n", a * b); break;
        case '/': 
            if (b != 0)
                printf("Result = %.2f\n", a / b);
            else
                printf("Error: Division by zero\n");
            break;
        default: printf("Invalid operator\n");
    }

    return 0;
}

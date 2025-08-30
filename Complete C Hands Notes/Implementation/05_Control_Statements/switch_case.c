#include <stdio.h>

int main() {
    int choice;
    printf("Enter 1 for Tea, 2 for Coffee: ");
    scanf("%d", &choice);

    switch(choice) {
        case 1: printf("You chose Tea\n"); break;
        case 2: printf("You chose Coffee\n"); break;
        default: printf("Invalid choice\n");
    }

    return 0;
}

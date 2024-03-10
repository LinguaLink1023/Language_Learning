#include <stdio.h>
#include <math.h>
#include <iso646.h>
#include <stdbool.h>

typedef double real;

int main() {
    char ch = 'a';
    switch (ch) {
        case 'a':
            printf("Apple\n");
            break;
        case 'b':
            printf("Banana\n");
            break;
        case 'c':
            printf("Cherry\n");
            break;
        default:
            printf("Last one\n");
            break;
    }
}
#include <stdio.h>
#include <math.h>
#include <iso646.h>
#include <stdbool.h>

typedef double real;

int main() {
    bool canDo = true;
    int number = 0;
    if (canDo) {
        number = 100;
    } else {
        number = 59;
    }
    printf("number = %d\n", number);
    return 0;
}
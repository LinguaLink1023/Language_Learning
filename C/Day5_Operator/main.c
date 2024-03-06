#include <stdio.h>
#include <math.h>

int main() {
    int scale = 2.0, n = 3;
    printf("25.0 + 99.0 * n / scale = %f\n", 25.0 + 99.0 * n / scale);
    printf("(25.0 + 99.0 * n) / scale = %f\n", (25.0 + 99.0 * n) / scale);
    printf("(25.0 + 99.0) * n / scale = %f\n", (25.0 + 99.0) * n / scale);
    return 0;
}
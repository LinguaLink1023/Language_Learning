#include <stdio.h>
#include <math.h>
typedef double real;

int main() {
    int GOLD_COUNTS = 999;// 假设这个变量是别人定义的
    double perGrame = 655.34;
    int total_cost = GOLD_COUNTS * (int)perGrame;
    printf("total_cost = %d\n", total_cost);
    printf("sizeof(perGrame) = %zd\n", sizeof perGrame);
    printf("sizeof((double)perGrame) = %zd\n", sizeof ((int)perGrame));
    return 0;
}
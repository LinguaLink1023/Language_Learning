#include <stdio.h>
#define BIRD "BLUE"
#include <stdbool.h>

// 泛型函数来打印整数的每一位二进制数
void printBits(size_t const size, void const * const ptr) {
    // 8位为一组进行打印
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    // 从高位字节开始处理
    for (i = size-1; i >= 0; i--) {
        // 获取当前字节
        byte = b[i];
        // 打印当前字节的每一位
        for (j = 7; j >= 0; j--) {
            // 使用位掩码来检查每一位
            unsigned char bit = (byte >> j) & 1;
            printf("%u", bit);
        }

        // 每打印完8位后添加一个空格，除了最后一组
        if (i > 0) {
            printf(" ");
        }
    }
    printf("\n");
}


typedef union {
    float f;
    struct {
        unsigned int mantissa : 23;
        unsigned int exponent : 8;
        unsigned int sign : 1;
    } parts;
} float_cast;

void printFloatBits(float f) {
    float_cast d1 = { .f = f };
    printf("%u ", d1.parts.sign);

    for (int i = 7; i >= 0; i--) {
        printf("%u", (d1.parts.exponent >> i) & 1);
    }

    printf(" ");

    for (int i = 22; i >= 0; i--) {
        printf("%u", (d1.parts.mantissa >> i) & 1);
    }
    
    printf("\n");
}


int main() {
    float f1 = -28.14;


    return 0;
}

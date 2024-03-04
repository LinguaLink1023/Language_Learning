#include <stdio.h>
#define BIRD "BLUE"

int main() {
    int age;
    char blood_type;
    float height;
    double weight;
    char description[30];
    printf("请依次输入你的年龄，血型，身高和体重:\n");
    scanf("%x,%c,%f,%lf", &age, &blood_type, &height, &weight);
    printf("你的信息如下:\n身高:%d\n血型:%c\n身高%.2fcm\n体重:%.2fkg\n", age, blood_type, height, weight);
    printf("输入你的描述:\n");
    scanf("%s", description);
    printf("你的自我描述:\n");
    printf("%s\n", description);
    return 0;
}

#include <stdio.h>

int main(){
    int a = 10;
    int b = a + 10;
    printf("a=%d b=%d\n", a, b);
    a = 20;
    printf("a=%d b=%d\n", a, b);
    // 这里就说明C语言的赋值区别于Python，python是引用，C是传递值
}

/*
占位符：
%d 十进制整数
%s 字符串
%p 指针
*/
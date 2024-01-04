#include<stdio.h>
int main()
{
    int num;
    printf("请输入一个整数，按回车结束。");
    scanf("%d",&num);
    if(num%2==0&&num%3==0)
    printf("%d可以被2,3整除",num);
    else
    printf("%d不可以被2,3整除",num);
    return 0;
}
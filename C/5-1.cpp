#include<stdio.h>
int main()
{
    int i=1,sum=0;//定义整形变量i，sum并初始化
    while(i<=100)//表达式成立并进行循环
        {
           sum=sum+i*i;
           i++;
        }
    printf("1^2+2^2+3^2+...+100^2=%d",sum);//输出求和结果
    return 0;
}
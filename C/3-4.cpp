#include<stdio.h>
int main()
{
    printf("请输入一个大写字母。");
	char ch1,ch2;
    ch1=getchar();
    ch2=ch1+32;
    putchar(ch2);
	printf("%d\n",ch1);
    return 0; 
}
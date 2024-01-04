#include<stdio.h>
int main()
{
	char a[100],*p;
	int b[100],*q;
	printf("请输入一个包含数字及非数字的字符串：");
	scanf("%s",a);
	p=a;
	for(i=0;*p!='\0';i++)
		if('0'<=a[i]&&a[i]<='9')
}
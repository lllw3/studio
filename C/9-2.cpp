#include<stdio.h>
#include<string.h>
int length(char*p,char*z);
int main()
{
	char a[100];
	char*p;
	printf("������һ���ַ�����\n");
	scanf("%s",a);
    length(p,a);
	printf("����Ϊ%d\n",length(p,a));
	return 0;
}
int length(char*p,char*z)
{
	p=z;
	while(*p!='\0')
		p++;
	return(p-z);
}
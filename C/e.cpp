#include<stdio.h>
int main()
{
	printf("������һ������λ���������س�����");
		int num,a,b,c;
	scanf("%d",&num);
	a=num/100;
	b=(num-a*100)/10;
	c=(num-a*100-b*10);
	printf("��λ%d,ʮλ%d,��λ%d/n",a,b,c);
	return 0;
}
#include<stdio.h>
void main()
{
    int money,a,b,c,d,e,f;
    printf("�����빤�ʽ����س�������\n");
    scanf("%d\n",&money);	
	printf("���ʽ�%d\n",money);
	a=money/100;
	money%=100;
    b=money/50;
	money%=50;
    c=money/20;
	money%=20;
    d=money/10;
	money%=10;
    e=money/5;
	f=money%5;
	printf("100Ԫ %4d��\n",a);
    printf("50Ԫ %4d��\n",b);
    printf("20Ԫ %4d��\n",c);
    printf("10Ԫ %4d��\n",d);
    printf("5Ԫ %4d��\n",e);
    printf("1Ԫ %4d��\n",f);
    
}
#include<stdio.h>
void main()
{
    int money,a,b,c,d,e,f;
    printf("请输入工资金额，按回车结束。\n");
    scanf("%d\n",&money);	
	printf("工资金额；%d\n",money);
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
	printf("100元 %4d张\n",a);
    printf("50元 %4d张\n",b);
    printf("20元 %4d张\n",c);
    printf("10元 %4d张\n",d);
    printf("5元 %4d张\n",e);
    printf("1元 %4d张\n",f);
    
}
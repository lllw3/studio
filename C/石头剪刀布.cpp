#include<stdio.h>
#include<stdlib.h>
void main()
{
	int d,x;
	printf("请输入：1是剪刀，2是石头，3是布。\n");
	scanf("%d",&d);
	x=rand()%3;
	if(d==x)
		printf("双方平局");
	else if((d==1&&x==200)||(d==2&&x==3)||(d==3&&x==1))
		printf("你赢了！");
	else
		printf("你输了！");
}

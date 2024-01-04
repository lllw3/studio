#include<stdio.h>
int main()
{
	printf("请输入一个人三位整数，按回车结束");
		int num,a,b,c;
	scanf("%d",&num);
	a=num/100;
	b=(num-a*100)/10;
	c=(num-a*100-b*10);
	printf("百位%d,十位%d,个位%d/n",a,b,c);
	return 0;
}
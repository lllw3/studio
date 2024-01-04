#include<stdio.h>
int main()
{
	int x,y,T;
	printf("请输入两个整数，用空格分开，按回车结束。\n");
	scanf("x=%d\n",&x);
	scanf("y=%d\n",&y);
	T=(2.0*x+3.0*y)/x;
	printf("%d\n",T);
	return 0;
}

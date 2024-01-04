#include<stdio.h>
double fun(double x);
int main()
{
	double x;
    printf("请输入汇款额：\n");
    scanf("%lf",&x);
    printf("应缴汇费为：%5.2f",fun(x));
	return 0;
}
double fun(double x)
{
	if(x<=500)
		return(5.5);
	else if(500<x&&x<=2000)
		return(0.02*x);
	else if(2000<x&&x<=5000)
		return(0.008*(x-2000)+40);
	else
		return(75*x);
}
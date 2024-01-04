#include<stdio.h>
#include<math.h>
int main()
{
	double x,y;
	printf("请输入一个实数x\n");
	scanf("%lf",&x);
	if(x<-3)
	{
		y=x-sin(x);
		printf("y=%.2lf\n",y);
	}
	else if(-3<=x&&x<=3)
	{
		y=pow(2.0,x)+x;
		printf("y=%.2lf\n",y);
	}
	else if(x>3)
	{
		y=sqrt(x*x+2.0*x+3.0);
        printf("y=%.2lf\n",y);
	}
	return 0;

}
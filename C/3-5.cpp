#include<stdio.h>
#include<math.h>
int main()
{
	float x,y,distance;
	printf("请输入x，y\n");//x,y为坐标点
	scanf("%f,%f",&x,&y);
	distance=sqrt(x*x+y*y);
	printf("其距离原点距离为：%f",distance);
	return 0;
}
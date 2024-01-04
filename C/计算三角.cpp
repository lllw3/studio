#include<stdio.h>
#include<math.h>
void main()
{
	float a,b,c,s,area;
	printf("请输入三角形三边，空格隔开，按回车结束：\n");
	scanf("%f%f%f",&a,&b,&c);
	s=(a+b+c)/2;
	area=sqrt(s*(s-a)*(s-b)*(s-c));
	printf("三角形三条边分别为：%5.2f %5.2f %5.2f\n",a,b,c);
	printf("三角形面积为：%f\n",area);
}
#include<stdio.h>
#include<math.h>
int main()
{
	float x,y,distance;
	printf("������x��y\n");//x,yΪ�����
	scanf("%f,%f",&x,&y);
	distance=sqrt(x*x+y*y);
	printf("�����ԭ�����Ϊ��%f",distance);
	return 0;
}
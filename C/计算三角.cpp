#include<stdio.h>
#include<math.h>
void main()
{
	float a,b,c,s,area;
	printf("���������������ߣ��ո���������س�������\n");
	scanf("%f%f%f",&a,&b,&c);
	s=(a+b+c)/2;
	area=sqrt(s*(s-a)*(s-b)*(s-c));
	printf("�����������߷ֱ�Ϊ��%5.2f %5.2f %5.2f\n",a,b,c);
	printf("���������Ϊ��%f\n",area);
}
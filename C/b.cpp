#include<stdio.h>
int main()
{
	double number1=0.0;//�����һ��������
	double number2=0.0;//����ڶ���������
	char operation=0;//operation�����ǡ�+�� ��-����*����/����%��

	printf("\nEnter the calculation\n");
	scanf("%1f%c%1f",&number1,&operation,&number2);
	return 0;
}
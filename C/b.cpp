#include<stdio.h>
int main()
{
	double number1=0.0;//定义第一个操作数
	double number2=0.0;//定义第二个操作数
	char operation=0;//operation必须是‘+’ ‘-’‘*’‘/’或‘%’

	printf("\nEnter the calculation\n");
	scanf("%1f%c%1f",&number1,&operation,&number2);
	return 0;
}
#include<stdio.h>
#include<string.h>
int main()
{
	char *month[]={"January","February","March","April","May","June","July","August","September","October","November","December"};
	int M;
	printf("please input  the month between 1 and 12:");
	scanf("%d",&M);
	if(M>=1&&M<=12)
		printf("the English is %s\n",*(month+M-1));
	else
		printf("error input!");
	return 0;
}
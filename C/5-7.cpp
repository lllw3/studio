#include<stdio.h>
int main()
{
	int k;
	for(k=1;k<=7;k++)
	{
		if(k%3==1)
			printf("**********\n");
		else
			printf("*        *\n");
	}
	return 0;
}
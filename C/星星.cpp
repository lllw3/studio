#include<stdio.h>
#include<math.h>
int main()
{
	int i,l;
	for(i=1;i<=7;i++)
	{
		if(i%3==1)
		{	for(l=1;l<=10;l++)
				printf("*");
			printf("\n");
		}
		else
        {
			printf("*");
		    for(l=1;l<=8;l++)
				printf(" ");
			printf("*\n");
		}
	}
	return 0;
}
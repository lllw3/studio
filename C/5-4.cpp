#include<stdio.h>
int main()
{
	int n1,n2,N;
	int n;
	printf("fibonaccis数列前30项为");
	n1=1;
	n2=1;
	N=1;
	for(n=0;n<30;n++)
	{
		if(n%6==0)
			printf("\n\r");
		 if((n==0)||(n==1))
			printf("%-7d",N);
		else
		{
			N=n1+n2;
			n1=n2;
			n2=N;
			printf("%-7d",N);
		}
	}
	printf("\n");
	return 0;
}
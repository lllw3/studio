#include<stdio.h>
int main()
{
	int i,j,k;
	for(i=1;i<=7;i++)
	{
		for(j=1;j<=7-i;j++)
			printf(" ");
		for(k=1;k<=2*i-1;k++)
			if(i%2==0)
				printf("%c",'$');
			else
				printf("%c",'@');
			printf("\n");
	}
	return 0;
}
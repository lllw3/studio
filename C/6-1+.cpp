#include<stdio.h>
int main()
{
	int i,j,a[10][10]={0};
	a[0][0]=1;
	printf("%3d",a[0][0]);
	for(i=3;i<10;i++){
		for(j=0;j<10;j++){
	      a[i][0]=1;
	      a[i][j]=a[i-1][j-1]+a[i-1][j];
		  if(a[i][j]==0)
			  printf(" ");
		  else
			  printf("%3d",a[i][j]);
		}
	   printf("\n");
	}
	return 0;
}
#include<stdio.h>
int main()
{
	int i,j;
	int a[3][4]={{1,2,3,4},{5,-6,7,8},{9,19,39,0}};
	int b[4][3];
	printf("����Ϊ��\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<4;j++)
		{
			printf("%5d",a[i][j]);
		}
		printf("\n");
	}
	for(i=0;i<3;i++){
		for(j=0;j<4;j++)
			b[j][i]=a[i][j];
	}
	printf("���жԵ���Ϊ��\n");
	for(i=0;i<4;i++){
		for(j=0;j<3;j++)
			printf("%5d",b[i][j]);
		printf("\n");
	}
}
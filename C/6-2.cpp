#include<stdio.h>
int main()
{
	int a[4][4];
	int i,j,sum1=0,sum2=0;
	printf("请输入16个数字。\n");
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			scanf("%d",&a[i][j]);
			printf("%2d ",a[i][j]);
			if(j==3)
				printf("\n");
		}
	}
    for(i=0;i<4;i++)
		sum1+=a[i][i];
	for(i=3,j=0;i>=0;i--){
		sum2+=a[i][j];
		j=j+1;
	}
	printf("该4*4整型矩阵对角线元素之和为%d。\n",sum1+sum2);
	return 0;

}
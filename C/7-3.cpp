#include<stdio.h>
int yh(int n);
int main()
{
	int n;
	printf("请输入参数n:\n");
	scanf("%d",&n);
     yh(n);
	return 0;
}

int yh(int n)
{
	int i,j;
	for(i=1;i<=n;i++){//行
		for(j=1;j<=n-i;j++)//列
			printf(" ");
		for(j=1;j<=i;j++)//前面数字
			printf("%d",j);
		for(j=1;j<=i-1;j++)//后面数字
			printf("%d",i-j);
		printf("\n");
	}
	return 0;
}
#include<stdio.h>
int yh(int n);
int main()
{
	int n;
	printf("���������n:\n");
	scanf("%d",&n);
     yh(n);
	return 0;
}

int yh(int n)
{
	int i,j;
	for(i=1;i<=n;i++){//��
		for(j=1;j<=n-i;j++)//��
			printf(" ");
		for(j=1;j<=i;j++)//ǰ������
			printf("%d",j);
		for(j=1;j<=i-1;j++)//��������
			printf("%d",i-j);
		printf("\n");
	}
	return 0;
}
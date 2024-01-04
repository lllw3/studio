#include<stdio.h>
/*求1！+2！+...+n!的总和*/
void Sum(int n){
	int fact=1,sum=0;
		for(int i=1;i<=n;i++){//控制加法 
		for(int a=1;a<=1;a++){//阶乘计算 
			fact=fact*i;
		}
		sum=sum+fact;
	}
	printf("1！+2！+...+%d!=%d",n,sum);
}
int main(){
	int n;
	printf("请输入正整数n：");
	scanf("%d",&n);
	Sum(n);
	return 0;
}

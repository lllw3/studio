#include<stdio.h>
/*��1��+2��+...+n!���ܺ�*/
void Sum(int n){
	int fact=1,sum=0;
		for(int i=1;i<=n;i++){//���Ƽӷ� 
		for(int a=1;a<=1;a++){//�׳˼��� 
			fact=fact*i;
		}
		sum=sum+fact;
	}
	printf("1��+2��+...+%d!=%d",n,sum);
}
int main(){
	int n;
	printf("������������n��");
	scanf("%d",&n);
	Sum(n);
	return 0;
}

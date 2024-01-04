#include<stdio.h>
/*求1！+2！+...+n!的总和*/
void SUM(int n){
	int fact=1,sum=0,a,i; 
	for(i=1;i<=n;i++){
		for(a=1;a<=i;i++){
			fact=a*fact; 
		}
		sum=sum+fact;
	}
	printf("1！+2！+...+n!=%d",sum); 
} 
int main(){
	int n;
	printf("请输入正整数n:\n");
	scanf("%d",&n);
	SUM(n);
	return 0;
} 

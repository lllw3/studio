#include<stdio.h>
/*��1��+2��+...+n!���ܺ�*/
void Sum(int n){
	int fact=1,sum=0,a,i;//
	for(i=1;i<=n;i++){
		for(a=1;a<=i;i++){
			fact=a*fact;
		}
		sum=sum+fact;
	}
	printf("1��+2��+...+n!=%d",sum); 
} 
int main(){
	int n;
	printf("������������n��"); 
	scanf("%d",&n); 
	Sum(n);
	return 0;
}

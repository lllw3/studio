#include<stdio.h>
#include<math.h> 
/*�����㷨ʱ�亯�����������Ʒ���*/ 
int factorial(int n){
	int x;
	double y=1;
	for(x=1;x<=n;x++){
		y=y*x;
	} 
	return y;
}
void exponent(int n,double num2,int num3,double num4,int num5,int num6,int num7){
	num2=sqrt(n);//�����n 
	num3=n;//��n 
	num4=log(n)/log(2)*n;//��nlog2��n�� 
	num5=pow(n,2);//��n��ƽ�� 
	num6=pow(n,3);//��n������ 
	num7=pow(2,n);//��2��n�η� 
}
void fun(int n){
	int num3,num5,num6,num7,num8;
	double num1,num2,num4;
	//num1Ϊ����������num2-num7Ϊ�ݺ�����num8Ϊ�׳�
	num1=log(n)/log(2);//��log2��n��
	exponent(n,num2,num3,num4,num5,num6,num7);
/*	num2=sqrt(n);//�����n 
	num3=n;//��n 
	num4=log(n)/log(2)*n;//��nlog2��n�� 
	num5=pow(n,2);//��n��ƽ�� 
	num6=pow(n,3);//��n������ 
	num7=pow(2,n);//��2��n�η�   */
	num8=factorial(n);//��n�Ľ׳�
	printf("log2(n)=%.2lf,��n=%.2lf,n=%d,nlog2(n)=%.2lf,n^2=%d,n^3=%d,2^n=%d,n!=%d",num1,num2,num3,num4,num5,num6,num7,num8); 
}
int main(){
	int n;
	for(n=1;n<=10;n++){
		fun(n);
		printf("\n");
	}
	return 0; 
}

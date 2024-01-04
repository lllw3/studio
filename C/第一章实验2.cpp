#include<stdio.h>
#include<math.h> 
/*常见算法时间函数的增长趋势分析*/ 
int factorial(int n){
	int x;
	double y=1;
	for(x=1;x<=n;x++){
		y=y*x;
	} 
	return y;
}
void exponent(int n,double num2,int num3,double num4,int num5,int num6,int num7){
	num2=sqrt(n);//求根号n 
	num3=n;//求n 
	num4=log(n)/log(2)*n;//求nlog2（n） 
	num5=pow(n,2);//求n的平方 
	num6=pow(n,3);//求n的立方 
	num7=pow(2,n);//求2的n次方 
}
void fun(int n){
	int num3,num5,num6,num7,num8;
	double num1,num2,num4;
	//num1为对数函数，num2-num7为幂函数，num8为阶乘
	num1=log(n)/log(2);//求log2（n）
	exponent(n,num2,num3,num4,num5,num6,num7);
/*	num2=sqrt(n);//求根号n 
	num3=n;//求n 
	num4=log(n)/log(2)*n;//求nlog2（n） 
	num5=pow(n,2);//求n的平方 
	num6=pow(n,3);//求n的立方 
	num7=pow(2,n);//求2的n次方   */
	num8=factorial(n);//求n的阶乘
	printf("log2(n)=%.2lf,√n=%.2lf,n=%d,nlog2(n)=%.2lf,n^2=%d,n^3=%d,2^n=%d,n!=%d",num1,num2,num3,num4,num5,num6,num7,num8); 
}
int main(){
	int n;
	for(n=1;n<=10;n++){
		fun(n);
		printf("\n");
	}
	return 0; 
}

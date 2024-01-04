#include<stdio.h>
#include<math.h>
#include<time.h>
/*求1-n素数个数并对比不同解法的绝对执行时间*/
bool Prime1(int n){
	for(int i=2;i<=n/2;i++){
		if(n%i==0)
		return false;
	}
	return true;
}
bool Prime2(int n){
	for(int i=2;i<=sqrt(n1);i++){
	if(n%i==0)
	return false;
	}
	return true;
}
/*以上为判断一个数n是否为素数*/
void PrimeTime1(int n){
	int x=0;
	for(int a=2;a<n;a++){
		if(Prime1(a))
		x++;
	}
	printf("1-n中素数的个数为%d\n",x);
} 
void PrimeTime2(int n){
	int x=0;
	for(int a=2;a<=n;a++){
		if(Prime2(a))
		x++;
	}
	printf("1-n中素数的个数为%d\n",x);
}
int main(){
	int n;
	printf("请输入正整数n：");
	scanf("%d",&n); 
	clock_t t1;
	t1=clock();
	PrimeTime1(n);
	t1=clock()-t1;
	printf("用时：%lf\n",((float)t1)/CLOCKS_PER_SEC);//输出所用时间
	clock_t t2;
	t2=clock();
	PrimeTime2(n);
	t2=clock()-t2;
	printf("用时：%lf\n",((float)t2)/CLOCKS_PER_SEC);//输出所用时间
	return 0;
}

#include<stdio.h>
#include<time.h>
//计算并测试1+...n的结果和时间。AddTime1为累加法，AddTime2为高斯法。 
void AddTime1(int n){
	int i;
	double sum=0;
	for(i=1;i<=n;i++){
		sum+=i;
	}
	printf("1+2+...+n=%lf\n",sum);
}
void AddTime2(int n){
	double sum;
	sum=(1+n)/2.0*n;
	printf("1+2+...+n=%lf\n",sum);	
}
int main(){
	int n; 
	printf("请输入n值，n为整数：\n");
	scanf("%d",&n);//从键盘输入n值 
    clock_t t1,t2;
	t1=clock();
	AddTime1(n);
	t1=clock()-t1;
	printf("用时：%lf\n",((double)t1)/CLOCKS_PER_SEC);//输出AddTime1所用时间 
	t2=clock();
	AddTime2(n);
	t2=clock()-t2;
	printf("用时：%lf\n",((double)t2)/CLOCKS_PER_SEC);//输出AddTime2所用时间 
	return 0;
}



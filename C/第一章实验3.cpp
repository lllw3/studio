#include<stdio.h>
#include<math.h>
#include<time.h>
/*��1-n�����������ԱȲ�ͬ�ⷨ�ľ���ִ��ʱ��*/
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
/*����Ϊ�ж�һ����n�Ƿ�Ϊ����*/
void PrimeTime1(int n){
	int x=0;
	for(int a=2;a<n;a++){
		if(Prime1(a))
		x++;
	}
	printf("1-n�������ĸ���Ϊ%d\n",x);
} 
void PrimeTime2(int n){
	int x=0;
	for(int a=2;a<=n;a++){
		if(Prime2(a))
		x++;
	}
	printf("1-n�������ĸ���Ϊ%d\n",x);
}
int main(){
	int n;
	printf("������������n��");
	scanf("%d",&n); 
	clock_t t1;
	t1=clock();
	PrimeTime1(n);
	t1=clock()-t1;
	printf("��ʱ��%lf\n",((float)t1)/CLOCKS_PER_SEC);//�������ʱ��
	clock_t t2;
	t2=clock();
	PrimeTime2(n);
	t2=clock()-t2;
	printf("��ʱ��%lf\n",((float)t2)/CLOCKS_PER_SEC);//�������ʱ��
	return 0;
}

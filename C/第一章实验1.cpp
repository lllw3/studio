#include<stdio.h>
#include<time.h>
//���㲢����1+...n�Ľ����ʱ�䡣AddTime1Ϊ�ۼӷ���AddTime2Ϊ��˹���� 
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
	printf("������nֵ��nΪ������\n");
	scanf("%d",&n);//�Ӽ�������nֵ 
    clock_t t1,t2;
	t1=clock();
	AddTime1(n);
	t1=clock()-t1;
	printf("��ʱ��%lf\n",((double)t1)/CLOCKS_PER_SEC);//���AddTime1����ʱ�� 
	t2=clock();
	AddTime2(n);
	t2=clock()-t2;
	printf("��ʱ��%lf\n",((double)t2)/CLOCKS_PER_SEC);//���AddTime2����ʱ�� 
	return 0;
}



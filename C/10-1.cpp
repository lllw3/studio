#include<stdio.h>
#include<malloc.h>
struct student
{
	int SID;//ѧ��ID
	double middle_score;//���гɼ�
	double final_score;//��ĩ�ɼ�
};//ѧ����Ϣ�ṹ��
int main(void)
{
	int n,total;
	struct student*pArr;
	pArr=(struct student*)malloc(total*sizeof(struct student));//��������
	printf("please input the number of student:\n");
	scanf("%d",&total);//���ѧ������
	for(n=0;n<total;n++)
	{
		printf("the %d student's information:\n",n+1);
		printf("SID=:");
		scanf("%d",&pArr[n].SID);
		printf("middle_score=");
		scanf("%lf",&pArr[n].middle_score);
		printf("final_score=");
		scanf("%lf",&pArr[n].final_score);		
	}//����ѧ����Ϣ
	printf("\n=================ѧ����Ϣ====================\n");
		for(n=0;n<total;++n)
	{
		printf("the %d student's information:\n",n+1);
		printf("SID=:%d  ",pArr[n].SID);
		printf("middle_score:%lf  ",pArr[n].middle_score);
		printf("final_score:%lf  ",pArr[n].final_score);
		printf("avarage:%lf",(pArr[n].middle_score+pArr[n].final_score)/2);//ƽ����
		printf("\n");
	}//���ѧ����Ϣ
	return 0;//��������
}
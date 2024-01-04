#include<stdio.h>
#include<malloc.h>
struct student
{
	int SID;//学生ID
	double middle_score;//期中成绩
	double final_score;//期末成绩
};//学生信息结构体
int main(void)
{
	int n,total;
	struct student*pArr;
	pArr=(struct student*)malloc(total*sizeof(struct student));//建立数组
	printf("please input the number of student:\n");
	scanf("%d",&total);//输出学生人数
	for(n=0;n<total;n++)
	{
		printf("the %d student's information:\n",n+1);
		printf("SID=:");
		scanf("%d",&pArr[n].SID);
		printf("middle_score=");
		scanf("%lf",&pArr[n].middle_score);
		printf("final_score=");
		scanf("%lf",&pArr[n].final_score);		
	}//输入学生信息
	printf("\n=================学生信息====================\n");
		for(n=0;n<total;++n)
	{
		printf("the %d student's information:\n",n+1);
		printf("SID=:%d  ",pArr[n].SID);
		printf("middle_score:%lf  ",pArr[n].middle_score);
		printf("final_score:%lf  ",pArr[n].final_score);
		printf("avarage:%lf",(pArr[n].middle_score+pArr[n].final_score)/2);//平均分
		printf("\n");
	}//输出学生信息
	return 0;//结束程序
}
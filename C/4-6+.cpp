#include<stdio.h>
int main()
{
     int e,m,s,d,t;//eΪ�����˷ѣ�mΪ������sΪ���룬dΪ�ۿۣ�tΪ���˷�
     printf("���������s:\n");
     scanf("%d",&s);
     if(s<200)
       d=0;//���������
     else if(s>=200&&s<600)
       d=3;//�ۿ�Ϊ3%���
     else if(s>=600&&s<1000)
       d=6;//�ۿ�Ϊ6%���
     else if(s>=1000&&s<2000) 
       d=9;//�ۿ�Ϊ9%���
     else if(s>=2000)
       d=11;//�ۿ�Ϊ11%���
	 t=e*m*s*(1-d/100);
     printf("���˷�tΪ%dԪ",t);//����˷�
     return 0;//��������
}
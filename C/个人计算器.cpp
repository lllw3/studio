#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#define PI 3.14
int jf()
{
    int a1,b1,a2,b2,m,n,i;
 printf("���ԡ�1/8 1/9��Ϊ��������������\n");
    scanf("%d/%d",&a1,&b1);
    scanf("%d/%d",&a2,&b2);
    m=b1*b2;
    n=a1*b2+a2*b1;
    if(n%m==0)printf("%d",n/m);
    else{
        for(i=2;i<=m&&i<=n;i++){
   if(n%i==0&&m%i==0){
    n=n/i;
    m=m/i;
    i--;
   }
        }
        printf("%d/%d\n ",n,m);
    }
    return 0;
}
int zuida()//��˸����������ֵ
{
 int i,j,arr[2][4],max=0;
 printf("������˸��������Կո�ָ���\n");
 for(i=0;i<=1;i++)
 {
  for(j=0;j<=3;j++)
  {
  scanf("%d",&arr[i][j]);
  }
 printf("\n");
 printf("--------------------------\n");
 }
 for(i=0;i<=1;i++)
 {
  for(j=0;j<=3;j++)
  {
   if(arr[i][j]>max)
   {
   max=arr[i][j];
   }
  }
 }
 return max;
}
long f(int n)//��һ�����Ľ׳�
{
 if(n<0||n>12)
  printf("n<0,input error\n");
 else if(n==0||n==1)
  return (1);
 else
  return(n*(f(n-1))); 
}
double qiu(double r)//�������
{
 return ((4.0/3)*PI*pow(r,3));
}
double yuanzhu()//Բ�����
{
 double i,h,j;
 printf("�밴��A B������ʽ��������Բ���ĵ���뾶�͸�\n");
 scanf("%lf %lf",&i,&h);
 printf("--------------------------\n");
 j=(PI*pow(i,2)*h);
 return j;
}
int main()
{
 while(1)
 {
  int x,n;
  long result;
  int i,j;
  double r;
  printf("    ------���˼�����------\n");
  printf("��ѡ��\n");
  printf("1,Բ�����   2,�������  3,�˷��ھ���  4,�ӷ��ھ���  5,��һ�����Ľ׳�  6,��˸����������ֵ 7.�������ӷ�\n");
  scanf("%d",&x);
 switch(x)
  {
 case 7:
  jf();
  break;
 case 6:
  printf("�˸����е����ֵΪ��%d\n",zuida());
  printf("--------------------------\n");
  break;
 case 5:
  printf("Input a integre numbers(0<=n<=12)\n");
  scanf("%d",&n);
  result=f(n);
  printf("%d!=%ld\n",n,result);
  break;
 case 4://�ӷ��ھ���
  for(i=1;i<10;i++)
  {
   for(j=i;j>0;j--)
   {
   printf("%d+%d=%d ",i,j,i+j);
   }
   printf("\n");
  }
  break;
 case 3://�˷��ھ���
  for(i=1;i<10;i++)
  {
   for(j=i;j>0;j--)
   {
   printf("%d*%d=%d ",i,j,i*j);
   }
   printf("\n");
  }
  break;
 case 2:
  printf("����������뾶��\n");
  scanf("%lf",&r);
  printf("--------------------------\n");
  printf("�������Ϊ��%.2lf\n",qiu(r));
  printf("--------------------------\n");
  break;
 case 1:
  printf("Բ�����Ϊ��%.2lf\n",yuanzhu());
  printf("--------------------------\n");
  break;
 default:
  printf("����������������룡\n");
  }
 system("pause");//��ͣ����
 system("cls");//��������
 }
 return 0;
}
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#define PI 3.14
int jf()
{
    int a1,b1,a2,b2,m,n,i;
 printf("请以“1/8 1/9”为例输入两个分数\n");
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
int zuida()//求八个整数的最大值
{
 int i,j,arr[2][4],max=0;
 printf("请输入八个整数，以空格分隔！\n");
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
long f(int n)//求一个数的阶乘
{
 if(n<0||n>12)
  printf("n<0,input error\n");
 else if(n==0||n==1)
  return (1);
 else
  return(n*(f(n-1))); 
}
double qiu(double r)//球体体积
{
 return ((4.0/3)*PI*pow(r,3));
}
double yuanzhu()//圆柱体积
{
 double i,h,j;
 printf("请按“A B”的形式依次输入圆柱的底面半径和高\n");
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
  printf("    ------个人计算器------\n");
  printf("请选择：\n");
  printf("1,圆柱体积   2,球体体积  3,乘法口诀表  4,加法口诀表  5,求一个数的阶乘  6,求八个整数的最大值 7.有理数加法\n");
  scanf("%d",&x);
 switch(x)
  {
 case 7:
  jf();
  break;
 case 6:
  printf("八个数中的最大值为：%d\n",zuida());
  printf("--------------------------\n");
  break;
 case 5:
  printf("Input a integre numbers(0<=n<=12)\n");
  scanf("%d",&n);
  result=f(n);
  printf("%d!=%ld\n",n,result);
  break;
 case 4://加法口诀表
  for(i=1;i<10;i++)
  {
   for(j=i;j>0;j--)
   {
   printf("%d+%d=%d ",i,j,i+j);
   }
   printf("\n");
  }
  break;
 case 3://乘法口诀表
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
  printf("请输入球体半径：\n");
  scanf("%lf",&r);
  printf("--------------------------\n");
  printf("球体体积为：%.2lf\n",qiu(r));
  printf("--------------------------\n");
  break;
 case 1:
  printf("圆柱体积为：%.2lf\n",yuanzhu());
  printf("--------------------------\n");
  break;
 default:
  printf("输入错误，请重新输入！\n");
  }
 system("pause");//暂停函数
 system("cls");//清屏函数
 }
 return 0;
}
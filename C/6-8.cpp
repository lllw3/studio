#include<stdio.h>
int main()
{
     int i,j;
     char str1[100],str2[100],str3[100],str4[100];
	 printf("请输入四个字符串，找出最大值。\n");
     gets(str1);
     gets(str2);
     gets(str3);
     gets(str4);
	 for(j=0;j<100;j++){
		 if(str1[j]>str2[j]&&str1[j]>str3[j]&&str1[j]>str4[j]){
             i=1;
		 }
         else if(str2[j]>str1[j]&&str2[j]>str3[j]&&str2[j]>str4[j]){
             i=2;
		 }
         else if(str3[j]>str1[j]&&str3[j]>str2[j]&&str3[j]>str4[j]){
             i=3;
		 }
         else if(str4[j]>str1[j]&&str4[j]>str2[j]&&str4[j]>str3[j]){
             i=4;
		 }
	 }
     switch(i)
	 {
       case 1:puts(str1);break;
       case 2:puts(str2);break;
       case 3:puts(str3);break;
       case 4:puts(str4);break;
	 }
     return 0;
}
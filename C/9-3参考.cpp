#include <stdio.h>
#include <string.h>
void sort(char*str[],int paixu)
{
	int i,j;
	char*temp;
	for(i=0;i<paixu-1;i++){
		for(j=i+1;j<paixu;j++){
			if(strcmp(str[i],str[j])>0){
				temp=str[i];
				str[i]=str[j];
				str[j]=temp;}
		}
	}
}
int main()
{
	char str[5][20];
	char*p[5];
	int i;
	printf("请输入五个字符串，回车隔开：\n");
	for(i=0;i<5;i++){
		scanf("%s",str[i]);
		p[i]=str[i];
	}
	sort(p,5);
	printf("排序后为：");
	for(i=0;i<5;i++)
	printf("%s ",p[i]);
	printf("\n");
}


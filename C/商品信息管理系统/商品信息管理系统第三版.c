/*
    为了解决商品库存信息在日常生活中易于丢失、遗忘，不易保存和管理的问题，我们设计商品库存管理系统，来帮助商家方便地对商品信息进行增加、删除、修改等日常维护，并且能进行商品信息的查询，从而能更全面直观地了解到商品库存信息。
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MaxSize 1000
typedef struct Product {
    int ID;//商品编号
    char Name[MaxSize];//商品名称
    char Producer[MaxSize];//商品生产商
    char Date[10];//商品生产日期 
    float Price;//商品价格
    int Amount;//商品数量
    struct Product* next;//指针域
    struct Product* pre;//指针域
}Product;//商品信息
Product* init() {
    Product* p = (Product*)malloc(sizeof(Product));
    if (!p) {
        printf("创建失败！程序即将退出\n");
        exit(-1);
    }
    p->next = NULL;
    p->pre = NULL;
    return p;
}
Product* head;
Product* findLastNode(Product* head) {
    Product* p = head;
    while (p->next) {
        p = p->next;
    }
    return p;
}
int findID(Product* head, int ID) {//查找ID
    Product* p = head;
    while (p->next) {
        p = p->next;
        if (p->ID == ID) {
            return 1;
        }
    }
    return 0;
}
int findName(Product* head, char* name) {//查找名称 
    Product* p = head;
    while (p->next) {
        p = p->next;
        if (!strcmp(p->Name,name)) {
            return 1;
        }
    }
    return 0;
}
Product* findIDNode(Product* head, int ID) {//通过指针查找商品ID 
    Product* p = head;
    while (p->next) {
        p = p->next;
        if (p->ID == ID) {
            return p;
        }
    }
    return NULL;
}
int findNameNumber(Product* head, char* name) {//查找同名商品数量 
    Product* p = head;
    int i = 0;
    while (p->next) {
        p = p->next;
        if (!strcmp(p->Name, name)) {
            i++;
        }
    }
    return i;
}
void findNameNode(Product* head, char* name, Product* array[]) {//通过指针查找商品名称 
    Product* p = head;
    int i = 0;
    while (p->next) {
        p = p->next;
        if (!strcmp(p->Name, name)) {
            array[i++] = p;
        }
    }
}
int traverse() {//输出格式
    int i = 0;
    Product* p = head;
    while (p->next) {
        i = 1;
        p = p->next;
        printf("%d\t\t%s\t\t%.2f\t\t%d\t\t%s\t\t%s\n", p->ID, p->Name, p->Price, p->Amount, p->Date, p->Producer);
    }
    return i;
}
void ShowMenu() {//主菜单 
    printf("\n\n\n\n\n");
    printf("\t\t|----------------PRODUCT-----------------|\n");
    printf("\t\t|        1.input record                  |\n");
    printf("\t\t|        2.output record                 |\n");
    printf("\t\t|        3.delete record                 |\n");
    printf("\t\t|        4.modify record                 |\n");
    printf("\t\t|        5.search record                 |\n");
    printf("\t\t|        6.show record                   |\n");
    printf("\t\t|        0.exit and save                 |\n");
    printf("\t\t|----------------------------------------|\n");
    printf("\n\t\t         choose<0-6>:");
}
/*    商品入库
        能够录入商品编号、名称、数量、价格、生产日期、供货商等信息，并支持连续输入多个商品信息
*/
Product* inputinfo() {//用户输入商品 
    Product* newNode;
    newNode = (Product*)malloc(sizeof(Product));
    printf("Id:");
    scanf("%d", &newNode->ID);
    printf("Name:");
    scanf("%s", newNode->Name);
    printf("Producer:");
    scanf("%s", newNode->Producer);
    while (1) {
        printf("Date<Example 2020-05-21>:");
        char date[MaxSize];
        scanf("%s", date);
        if (strlen(date) == 10 && date[4] == '-' && date[7] == '-') {
            if (date[6] == '0' && date[9] == '0') {
                printf("非法日期！\n");
            } else {
                strcpy(newNode->Date, date);
                break;
            }
        } else {
            printf("日期有误！\n");
        }
    }
    printf("Price:");
    scanf("%f", &newNode->Price);
    printf("Amount:");
    scanf("%d", &newNode->Amount);
    newNode->next = NULL;
    newNode->next = NULL;
    return newNode;
}
void InputProduct() {
    system("cls");
    printf("\t\t\t欢迎使用入库管理！\n");
    Product* preNode;
    Product* newNode;
    int ID;
    char input;
    printf("请输入 ID，查询是否在库：");
    scanf("%d", &ID);
    int flag = findID(head, ID);
    if (flag) {
        printf("the id is existing.\n");
        return;
    } else {
    	printf("是否创建商品：(Y/N)"); 
        getchar();
    	scanf("%c", &input);
    	if(input == 'y' || input == 'Y'){
        	printf("正在为您创建商品\n");
        	newNode = inputinfo();
        	preNode = findLastNode(head);
        	preNode->next = newNode;
        	newNode->pre = preNode;
        } else {
            return;
        }
	}
    printf("\t\t\t入库成功！\n");
    printf("\t\t\t祝您生意兴隆！再见！\n");
}
/*    商品出库
        根据用户输入要进行出库操作的商品编号，如果存在该商品，则可以输入要出库的商品数量，实现出库操作
*/
void OutputProduct() {
    system("cls");
    printf("\t\t\t欢迎使用出库管理！\n");
    Product* thisNode;
    int ID;
    int Amount;
    printf("请输入 ID，查询是否在库：");
    scanf("%d", &ID);
    int flag = findID(head, ID);
    if (flag) {
        printf("find the product\n");
        printf("input the amount to output:");
        scanf("%d", &Amount);
        thisNode = findIDNode(head, ID);
        if (thisNode->Amount - Amount < 0) {
            printf("the amount is less than your input!\n");
            return;
        } else if (thisNode->Amount - Amount == 0) {
            printf("output successfully! The Amount is 0 now.\n");
            thisNode->Amount -= Amount;
        } else if (thisNode->Amount - Amount > 0) {
            printf("output successfully!\n");
            thisNode->Amount -= Amount;
        }
    } else {
        printf("ID不存在！");
        return;
    }
    printf("\t\t\t出库成功！\n");
    printf("\t\t\t祝您生意兴隆！再见！\n");
}
/*    删除商品信息
        根据用户输入要进行删除的商品编号，如果找到该商品，则将该编号对应的商品名称等各项信息均删除
*/
void DeleteProduct() {
    system("cls");
    int ID;
    printf("请输入要删除的商品编号:");
    scanf("%d", &ID);
    //判断商品是否存在
    if (findID(head, ID)) {
        //指针改变,删除商品      
        Product* thisNode = findIDNode(head, ID);
        thisNode->pre->next = thisNode->next;
        if (thisNode->next) {
            thisNode->next->pre = thisNode->pre;
        }
        free(thisNode);
    } else {
        printf("该商品不存在！");
        return;
    }
    printf("删除商品成功！\n");
}
/*    修改商品信息
        根据用户输入的商品编号找到该商品，若该商品存在，则可以修改商品的各项信息
*/
void ModifyProduct() {
    system("cls");
    int ID;
    printf("请输入要修改的商品ID：");
    scanf("%d", &ID);
    Product* thisNode;
    //判断商品是否存在
    if (findID(head, ID)) {
        printf("该商品存在！\n");
        thisNode = findIDNode(head, ID);
        printf("编号:%d，名称:%s，价格:%.2f，数量:%d，生产日期:%s，生产商:%s\n", thisNode->ID, thisNode->Name, thisNode->Price, thisNode->Amount, thisNode->Date, thisNode->Producer);
        printf("商品信息修改为\n");
		printf("ID:");
        scanf("%d", &thisNode->ID);
        printf("NAME:");
        scanf("%s", thisNode->Name);
        printf("PRODUCTER:");
        scanf("%s", thisNode->Producer);
        while (1){
            printf("DATE(YYYY-MM-DD):");
            char date[MaxSize];
            scanf("%s", date);
            if (strlen(date) == 10 && date[4] == '-' && date[7] == '-') {
                if (date[6] == '0' && date[9] == '0') {
                    printf("非法日期！\n");
                } else {
                    strcpy(thisNode->Date, date);
                    break;
                }
            } else {
                printf("日期格式有误！\n");
            }
        }
        printf("PRICE:");
        scanf("%f", &thisNode->Price);
        printf("AMOUNT:");
        scanf("%d", &thisNode->Amount);
    } else {
        printf("该商品不存在！");
        return;
    }
    printf("修改商品成功！\n");
}
/*    查询商品信息
        可以显示所有商品的信息，也可以输入商品编号查询某一个商品的信息
*/
void Find_number() {
    int ID;
    printf("请输入你要查询的商品的编号：");
    scanf("%d", &ID);
    Product* thisNode;
    if (findID(head,ID)) {
        printf("已找到该商品信息\n");
        thisNode = findIDNode(head, ID);
        printf("货物信息：编号:%d，名称:%s，价格:%.2f，数量:%d，生产日期:%s，生产商:%s\n", thisNode->ID, thisNode->Name, thisNode->Price, thisNode->Amount, thisNode->Date, thisNode->Producer);
    } else {
        printf("没有此商品信息！\n");
    }
}
void Find_sname() {
    char name[MaxSize];
    int number, i = 0;
    printf(" 请输入要查找商品的名称：");
    scanf("%s", name);
    if (findName(head,name)) {
        printf("已找到该商品信息\n");
        number = findNameNumber(head, name);
        Product* array[MaxSize];
        findNameNode(head, name, array);
        while (i<number) {
            printf("货物信息：编号:%d，名称:%s，价格:%.2f，数量:%d，生产日期:%s，生产商:%s\n", array[i]->ID, array[i]->Name, array[i]->Price, array[i]->Amount, array[i]->Date, array[i]->Producer);
            i++;
        }
    } else {
        printf("没有此商品！\n");
    }
}
void Find() {
    printf("\t\t查询信息\n");
    while (1) {
        int x;
        printf("\t 1.按商品名称查询\n");
        printf("\t 2.按商品编号查询\n");
        printf("请输入你的选择：");
        scanf("%d", &x);
        if (x == 2) {
            Find_number();
            break;
        }
        if (x == 1) {
            Find_sname();
            break;
        } else {
            printf("输入错误！\n");
        }
    }
}
void SearchProduct() {
    system("cls");
    Find();
    printf("搜索商品完成！\n");
}
void ShowProduct() {
    system("cls");
    printf("id\t\tname\t\tprice\t\tamount\t\tdate\t\tproducer\n");
    int flag = traverse();
    if (!flag) {
        printf("没有商品信息！\n");
    }else
    printf("展示商品完毕！\n");
}
void saveToFile() {
    FILE* fp;
    Product* p = head;
    fp = fopen("info.txt", "w");
    fprintf(fp, "id\t\tname\t\tprice\t\tamount\t\tdate\t\tproducer\n");
    while (p->next) {
        p = p->next;
        fprintf(fp, "%d\t\t%s\t\t%.2f\t\t%d\t\t%s\t\t%s\n", p->ID, p->Name, p->Price, p->Amount, p->Date, p->Producer);
    }
    fclose(fp);
} 
int main() {
    head = init();
    while (1) {
        ShowMenu();
        int number;
        scanf("%d", &number);
        switch (number) {
        case 1:
            InputProduct();
            break;
        case 2:
            OutputProduct();
            break;
        case 3:
            DeleteProduct();
            break;
        case 4:
            ModifyProduct();
            break;
        case 5:
            SearchProduct();
            break;
        case 6:
            ShowProduct();
            break;
        case 0:
            printf("程序即将退出\n");
            system("pause");
            saveToFile();
            exit(0);
        default:
            printf("输入不正确，请重新输入");
        }
    }
    return 0;
}

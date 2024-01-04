/*
    Ϊ�˽����Ʒ�����Ϣ���ճ����������ڶ�ʧ�����������ױ���͹�������⣬���������Ʒ������ϵͳ���������̼ҷ���ض���Ʒ��Ϣ�������ӡ�ɾ�����޸ĵ��ճ�ά���������ܽ�����Ʒ��Ϣ�Ĳ�ѯ���Ӷ��ܸ�ȫ��ֱ�۵��˽⵽��Ʒ�����Ϣ��
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MaxSize 1000
typedef struct Product {
    int ID;//��Ʒ���
    char Name[MaxSize];//��Ʒ����
    char Producer[MaxSize];//��Ʒ������
    char Date[10];//��Ʒ�������� 
    float Price;//��Ʒ�۸�
    int Amount;//��Ʒ����
    struct Product* next;//ָ����
    struct Product* pre;//ָ����
}Product;//��Ʒ��Ϣ
Product* init() {
    Product* p = (Product*)malloc(sizeof(Product));
    if (!p) {
        printf("����ʧ�ܣ����򼴽��˳�\n");
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
int findID(Product* head, int ID) {//����ID
    Product* p = head;
    while (p->next) {
        p = p->next;
        if (p->ID == ID) {
            return 1;
        }
    }
    return 0;
}
int findName(Product* head, char* name) {//�������� 
    Product* p = head;
    while (p->next) {
        p = p->next;
        if (!strcmp(p->Name,name)) {
            return 1;
        }
    }
    return 0;
}
Product* findIDNode(Product* head, int ID) {//ͨ��ָ�������ƷID 
    Product* p = head;
    while (p->next) {
        p = p->next;
        if (p->ID == ID) {
            return p;
        }
    }
    return NULL;
}
int findNameNumber(Product* head, char* name) {//����ͬ����Ʒ���� 
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
void findNameNode(Product* head, char* name, Product* array[]) {//ͨ��ָ�������Ʒ���� 
    Product* p = head;
    int i = 0;
    while (p->next) {
        p = p->next;
        if (!strcmp(p->Name, name)) {
            array[i++] = p;
        }
    }
}
int traverse() {//�����ʽ
    int i = 0;
    Product* p = head;
    while (p->next) {
        i = 1;
        p = p->next;
        printf("%d\t\t%s\t\t%.2f\t\t%d\t\t%s\t\t%s\n", p->ID, p->Name, p->Price, p->Amount, p->Date, p->Producer);
    }
    return i;
}
void ShowMenu() {//���˵� 
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
/*    ��Ʒ���
        �ܹ�¼����Ʒ��š����ơ��������۸��������ڡ������̵���Ϣ����֧��������������Ʒ��Ϣ
*/
Product* inputinfo() {//�û�������Ʒ 
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
                printf("�Ƿ����ڣ�\n");
            } else {
                strcpy(newNode->Date, date);
                break;
            }
        } else {
            printf("��������\n");
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
    printf("\t\t\t��ӭʹ��������\n");
    Product* preNode;
    Product* newNode;
    int ID;
    char input;
    printf("������ ID����ѯ�Ƿ��ڿ⣺");
    scanf("%d", &ID);
    int flag = findID(head, ID);
    if (flag) {
        printf("the id is existing.\n");
        return;
    } else {
    	printf("�Ƿ񴴽���Ʒ��(Y/N)"); 
        getchar();
    	scanf("%c", &input);
    	if(input == 'y' || input == 'Y'){
        	printf("����Ϊ��������Ʒ\n");
        	newNode = inputinfo();
        	preNode = findLastNode(head);
        	preNode->next = newNode;
        	newNode->pre = preNode;
        } else {
            return;
        }
	}
    printf("\t\t\t���ɹ���\n");
    printf("\t\t\tף��������¡���ټ���\n");
}
/*    ��Ʒ����
        �����û�����Ҫ���г����������Ʒ��ţ�������ڸ���Ʒ�����������Ҫ�������Ʒ������ʵ�ֳ������
*/
void OutputProduct() {
    system("cls");
    printf("\t\t\t��ӭʹ�ó������\n");
    Product* thisNode;
    int ID;
    int Amount;
    printf("������ ID����ѯ�Ƿ��ڿ⣺");
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
        printf("ID�����ڣ�");
        return;
    }
    printf("\t\t\t����ɹ���\n");
    printf("\t\t\tף��������¡���ټ���\n");
}
/*    ɾ����Ʒ��Ϣ
        �����û�����Ҫ����ɾ������Ʒ��ţ�����ҵ�����Ʒ���򽫸ñ�Ŷ�Ӧ����Ʒ���Ƶȸ�����Ϣ��ɾ��
*/
void DeleteProduct() {
    system("cls");
    int ID;
    printf("������Ҫɾ������Ʒ���:");
    scanf("%d", &ID);
    //�ж���Ʒ�Ƿ����
    if (findID(head, ID)) {
        //ָ��ı�,ɾ����Ʒ      
        Product* thisNode = findIDNode(head, ID);
        thisNode->pre->next = thisNode->next;
        if (thisNode->next) {
            thisNode->next->pre = thisNode->pre;
        }
        free(thisNode);
    } else {
        printf("����Ʒ�����ڣ�");
        return;
    }
    printf("ɾ����Ʒ�ɹ���\n");
}
/*    �޸���Ʒ��Ϣ
        �����û��������Ʒ����ҵ�����Ʒ��������Ʒ���ڣ�������޸���Ʒ�ĸ�����Ϣ
*/
void ModifyProduct() {
    system("cls");
    int ID;
    printf("������Ҫ�޸ĵ���ƷID��");
    scanf("%d", &ID);
    Product* thisNode;
    //�ж���Ʒ�Ƿ����
    if (findID(head, ID)) {
        printf("����Ʒ���ڣ�\n");
        thisNode = findIDNode(head, ID);
        printf("���:%d������:%s���۸�:%.2f������:%d����������:%s��������:%s\n", thisNode->ID, thisNode->Name, thisNode->Price, thisNode->Amount, thisNode->Date, thisNode->Producer);
        printf("��Ʒ��Ϣ�޸�Ϊ\n");
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
                    printf("�Ƿ����ڣ�\n");
                } else {
                    strcpy(thisNode->Date, date);
                    break;
                }
            } else {
                printf("���ڸ�ʽ����\n");
            }
        }
        printf("PRICE:");
        scanf("%f", &thisNode->Price);
        printf("AMOUNT:");
        scanf("%d", &thisNode->Amount);
    } else {
        printf("����Ʒ�����ڣ�");
        return;
    }
    printf("�޸���Ʒ�ɹ���\n");
}
/*    ��ѯ��Ʒ��Ϣ
        ������ʾ������Ʒ����Ϣ��Ҳ����������Ʒ��Ų�ѯĳһ����Ʒ����Ϣ
*/
void Find_number() {
    int ID;
    printf("��������Ҫ��ѯ����Ʒ�ı�ţ�");
    scanf("%d", &ID);
    Product* thisNode;
    if (findID(head,ID)) {
        printf("���ҵ�����Ʒ��Ϣ\n");
        thisNode = findIDNode(head, ID);
        printf("������Ϣ�����:%d������:%s���۸�:%.2f������:%d����������:%s��������:%s\n", thisNode->ID, thisNode->Name, thisNode->Price, thisNode->Amount, thisNode->Date, thisNode->Producer);
    } else {
        printf("û�д���Ʒ��Ϣ��\n");
    }
}
void Find_sname() {
    char name[MaxSize];
    int number, i = 0;
    printf(" ������Ҫ������Ʒ�����ƣ�");
    scanf("%s", name);
    if (findName(head,name)) {
        printf("���ҵ�����Ʒ��Ϣ\n");
        number = findNameNumber(head, name);
        Product* array[MaxSize];
        findNameNode(head, name, array);
        while (i<number) {
            printf("������Ϣ�����:%d������:%s���۸�:%.2f������:%d����������:%s��������:%s\n", array[i]->ID, array[i]->Name, array[i]->Price, array[i]->Amount, array[i]->Date, array[i]->Producer);
            i++;
        }
    } else {
        printf("û�д���Ʒ��\n");
    }
}
void Find() {
    printf("\t\t��ѯ��Ϣ\n");
    while (1) {
        int x;
        printf("\t 1.����Ʒ���Ʋ�ѯ\n");
        printf("\t 2.����Ʒ��Ų�ѯ\n");
        printf("���������ѡ��");
        scanf("%d", &x);
        if (x == 2) {
            Find_number();
            break;
        }
        if (x == 1) {
            Find_sname();
            break;
        } else {
            printf("�������\n");
        }
    }
}
void SearchProduct() {
    system("cls");
    Find();
    printf("������Ʒ��ɣ�\n");
}
void ShowProduct() {
    system("cls");
    printf("id\t\tname\t\tprice\t\tamount\t\tdate\t\tproducer\n");
    int flag = traverse();
    if (!flag) {
        printf("û����Ʒ��Ϣ��\n");
    }else
    printf("չʾ��Ʒ��ϣ�\n");
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
            printf("���򼴽��˳�\n");
            system("pause");
            saveToFile();
            exit(0);
        default:
            printf("���벻��ȷ������������");
        }
    }
    return 0;
}

#include<stdio.h>
 #include<string.h> 
 int Mode; 
 struct Box 
 { int unique_id, length, breadth, height, weight ; 
 char colour[30];
  struct Box*next;
}; struct Box *head;

void lastinsert ();
void display();
void search();
 void count(); 
 void Avg_Vol();
  void Diff_Vol(); 
  void Max_Height(); 
  void Update_weight();
   void Delete_by_Id();

int main() {

printf("\nAvailable Operations\n");
printf("\n1. Add_Boxes, , \n2. Display, \n3. Find_Box, \n4. Count, \n5. Avg_Vol, \n6. Min_Max_Vol_diff, \n7. Max_Height, \n8. Weight_Update, \n9. RemoveBoxBy_Id, \n10. EXIT");
printf("\nEnter your choice\n");

 scanf("%d", &Mode);
 
 
  switch(Mode)
{
         case 1:  
          lastinsert();  
        break;  
        case 2:  
             display();          
        break;  
        case 3:  
            search();     
        break;  
        case 4:  
           count();       
        break;  
        case 5:  
         Avg_vol();        
        break;  
        case 6:  
         Diff_Vol();          
        break;  
        case 7: 
         Max_height();
        break;  
        case 8:  
         Update_weight();
        break;  
        case 9:  
         delete_by_Id();
        case 10;
        exit(0);  
        break;
    default:
        printf("Please enter valid choice..\n");
}


void lastinsert()  
{
struct Box *ptr,*temp;
ptr = (struct *)malloc(sizeof(struct Box));
if(ptr == NULL)
{
printf("\nOVERFLOW");
}
else
{
printf("\nEnter Unique ID for the BOX :");
        scanf("%d",ptr->unique_id);
    
         printf("\nEnter Length for the BOX : ");
        scanf("%d",ptr->length);
    
         printf("\nEnter Breadth for the BOX : ");
        scanf("%d",ptr->breadth);
    
        printf("\nEnter Height for the BOX : ");
        scanf("%d",ptr->height);

        printf("\nEnter Color for the BOX : ");
        scanf("%s",ptr->color);

        printf("\nEnter Height for the BOX : ");
        scanf("%d",ptr->weight);

ptr->length = length;
if(head == NULL)
{
ptr -> next = NULL;
head = ptr;
printf("\nBox values inserted on 1st number");
}
else
{
temp = head;
while (temp -> next != NULL)
{
temp = temp -> next;
}
temp->next = ptr;
ptr->next = NULL;
printf("\nBox value inserted");

    }  
}  
}

void display()  
{
struct Box *ptr;
ptr = head;
if(ptr == NULL)
{
printf("No Boxes to Show");
}
else
{
printf("\nprinting values . . . . .\n");
while (ptr!=NULL)
{
printf("\n%d",ptr->data);
printf ("unique_id = %d\n, length = %d\n, breadth = %d\n, height =%d\n, color = %s", ptr->runique_id, ptr->length, ptr->breadth, ptr->height, ptr->color);

ptr = ptr -> next;
}
}
}

void search()  
{
struct Box *ptr;
int given_id,i=0,flag;
ptr = head;
if(ptr == NULL)
{
printf("\nEmpty List there \n");
}
else
{
printf("\nEnter Box Id which you want to search\n");
scanf("%d",&given_id);
while (ptr!=NULL)
{
if(ptr-> == item)
{
printf("item found at location %d ",i+1);
flag=0;
}
else
{
flag=1;
}
i++;
ptr = ptr -> next;
}
if(flag==1)
{
printf("Item not found\n");
}
}

}

void update_weight()
{
int i,loc,item;
struct node *ptr, *temp;
ptr = (struct node *) malloc (sizeof(struct node));
if(ptr == NULL)
{
printf("\nOVERFLOW");
}
else
{
printf("\nEnter element value");
scanf("%d",&item);
ptr->data = item;
printf("\nEnter the location after which you want to insert ");
scanf("\n%d",&loc);
temp=head;
for(i=0;i<loc;i++)
{
temp = temp->next;
if(temp == NULL)
{
printf("\ncan't insert\n");
return;
}

    }  
    ptr ->next = temp ->next;   
    temp ->next = ptr;   
    printf("\nNode inserted");  
}  
}


void Delete_by_Id()  
{  
    struct node *ptr,*ptr1;  
    int loc,i;    
    printf("\n Enter the unique ID of the  after which you want to perform deletion \n");  
    scanf("%d",&loc);  
    ptr=head;  
    for(i=0;i<loc;i++)  
    {  
        ptr1 = ptr;       
        ptr = ptr->next;  
              
        if(ptr == NULL)  
        {  
            printf("\nCan't delete");  
            return;  
        }  
    }  
    ptr1 ->next = ptr ->next;  
    free(ptr);  
    printf("\nDeleted node %d ",loc+1);  
}  


return 0; }

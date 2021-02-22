#include<stdio.h> 
#include<string.h>
#include<string.h>
#include<stdlib.h>
 
 void lastinsert();  
void display();  
void search();
void count();//mine
void Avg_Vol();
void Diff_Vol();
void Max_Height();
void update_weight(); 
void delete_by_Id();//mine
 
 struct Box
{ 
    int unique_id, length, breadth, height, weight;
    float volume;
   char color[30];
   struct Box*next;
   
}; 
struct Box *head;

int main() 
{  
    int Mode;
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
             Avg_Vol();        
            break;  
            case 6:  
             Diff_Vol();          
            break;  
            case 7: 
             Max_Height();
            break;  
            case 8:  
             update_weight();
            break;  
            case 9:  
               delete_by_Id();
        default:
            printf("Please enter valid choice..\n");
    }
}
    
    
    void lastinsert()  
{  
    struct Box* ptr;
    struct Box* temp;  
       
    ptr = (struct Box*)malloc(sizeof(struct Box*));      
    if(ptr == NULL)  
    {  
        printf("\nOVERFLOW");     
    }  
    else  
    {  
     printf("\nEnter Length for the BOX : ");
    scanf("%u",&ptr->length);

     printf("\nEnter Breadth for the BOX : ");
    scanf("%d",&ptr->breadth);

    printf("\nEnter Height for the BOX : ");
    scanf("%d",&ptr->height);

    printf("\nEnter Color for the BOX : ");
    scanf("%s",ptr->color);

    printf("\nEnter Height for the BOX : ");
    scanf("%d",&ptr->height);
        if(head == NULL)  
        {  
            ptr -> next = NULL;  
            head = ptr;  
            printf("\nBox values inserted on 1st");  
        }  
        else  
        {  
            temp = head;  
            while (temp -> next != NULL)  
            {  
                temp=temp->next;  
            }  
            temp->next = ptr;  
            ptr->next = NULL;  
            printf("\nBox value inserted");  
          
        }  
    }  
    free(ptr);
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
            printf("\n%d",ptr->length);  
            ptr = ptr -> next;  
        }  
    }  
}     

    void search()  
{  
    struct Box *ptr;  
    int box_Id;
    int i=0;
    int flag;  
    ptr = head;   
    if(ptr == NULL)  
    {  
        printf("\nEmpty List there \n");  
    }  
    else  
    {   
        printf("\nEnter Box Id which you want to search\n");   
        scanf("%d",&box_Id);
        while (ptr!=NULL)  
        {  
            if(ptr->unique_id == box_Id)  
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
    
 
 
 /*void update_weight()  
{  
    int i,loc,boxid;   
    struct Box *ptr;
     struct Box *temp;
      ptr = (struct Box*)malloc(sizeof(struct Box*));      
    if(ptr == NULL)  
    {  
        printf("\nOVERFLOW");  
    }  
    else  
    {  
        printf("\nEnter unique ID where to update weight ");  
        scanf("%d",&boxid);  
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
                return 0;  
            }  
          
        }  
        ptr ->next = temp ->next;   
        temp ->next = ptr;   

        printf("Node inserted");  
    }  
}  
*/

void count ()
{   
   int counter=0;
    struct Box *ptr;  
    ptr = head;   
    if(ptr == NULL)  
    {  
        printf("No Boxes to found");  
    }  
    else  
    {  
    
        while (ptr!=NULL)  
        {  
           counter++;
            ptr = ptr -> next;  
        }  
    }  
         printf("\nTotal number of boxes are %d\n", counter);    

}


void delete_by_Id()
{ 
    struct Box *ptr;   
    struct Box *ptr1;

    int box_Id;
    int i=0;
    int flag;  
    ptr = head;   
    if(ptr == NULL)  
    {  
        printf("\nEmpty List there \n");  
    }  
    else  
    {   
        printf("\nEnter Box Id which you want to delete\n");   
        scanf("%d",&box_Id);  
        while (ptr!=NULL)  
        {  

              ptr1 = ptr;      
            if(ptr->unique_id ==box_Id)  
            {  
                printf("item found of unique Id %d ", ptr->unique_id);  
                ptr1-> next = ptr ->next;  
                free(ptr);  
                flag=0;  
            }   
            else  
            {  
                flag=1;  
            }  
            
            ptr = ptr -> next;  
        }  
        if(flag==1)  
        {  
            printf("Item not found\n");  
        }  
    }     
   printf ("unique_id = %d, length = %d, breadth = %d, height =%d\n, color = %s", ptr->unique_id, ptr->length, ptr->breadth, ptr->height, ptr->color); 
} 

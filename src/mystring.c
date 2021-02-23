#include"mystring.h"



  int mystrlen(char *str1)
{
    int i=0,length=0;
    for(i=0;str1[i]!='\0';i++)
    {
       length++;                                                                                             
    }    
    return length;
}


char *mystrcat(char *str1,char *str2)
{
     int leng1=0,leng2=0,i=0,j=0;


     leng1=mystrlen(str1);
     leng2=mystrlen(str2);
     for(i=leng1;str2[j]!='\0';i++,j++)
     {
         str1[i]=str2[j];
     }
     str1[i]='\0';
   
     return str1;
}



int mystrcmp(char *str1,char *str2)
{
     int leng1=0,leng2=0,i=0,count=0;
     leng1=mystrlen(str1);
     leng2=mystrlen(str2);
     if(leng1==leng2)
     {
         for(i=0;i<leng1;i++)
         {
             if(str1[i]!=str2[i])
             {
                 return -1; 
             }
             else
             {
                 count++;
             }
         }
         if(count==leng1)
         {
             return 0;
         }
     }
     else
     {

         return leng1-leng2;
     }
}




  char *mystrcpy( const char *source_string,  char *new_string ) 
{
    int i;
    for(i=0;source_string[i]!='\0';i++)
    {
        new_string[i]=source_string[i];
    }
    new_string[i]= '\0';
    return new_string;
}

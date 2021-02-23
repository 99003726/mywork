#include"myutils.h"


 int factorial()

 {

    int i,fact=1,number;    
    printf("Enter a number: ");    
    scanf("%d",&number);    
    for(i=1;i<=number;i++)
    {    
        fact=fact*i;    
    }    
    printf("Factorial of %d is: %d",number,fact);    
    return 0;  
}


  int isPrime()
  {

      int n,i,m=0,flag=0;    
printf("Enter the number to check prime:");    
scanf("%d",&n);    
m=n/2;    
for(i=2;i<=m;i++)    
{    
if(n%i==0)    
{    
printf("Number is not prime");    
flag=1;    
break;    
}    
}    
if(flag==0)    
printf("Number is prime");     
return 0;  
  }

 int isPalindrome()

 {
int n,r,sum=0,temp;    
printf("enter the number=");    
scanf("%d",&n);    
temp=n;    
while(n>0)    
{    
r=n%10;    
sum=(sum*10)+r;    
n=n/10;    
}    
if(temp==sum)    
printf("palindrome number ");    
else    
printf("not palindrome");   
return 0;  


 }

 int vsum(int num,...) 
 {

   va_list valist;
   double sum = 0.0;
   int i;

   /* initialize valist for num number of arguments */
   va_start(valist, num);

   for (i = 0; i < num; i++)
    {
      sum += va_arg(valist, int);
   }

   va_end(valist);

   return sum;
}

 
 

#include"bitmask.h"


  int set(int input,int n)
{  int n, input;
     printf("Enter your input value:");
     scanf("%d", &input);
     printf("Enter the value for n(nth bit):");
     scanf("%d", &n);
    input = input | (1 << n);
     printf("Result: %d\n", input);

                     
}
  int reset(int input,int n)
{
  int n, input;
     printf("Enter your input value:");
     scanf("%d", &input);
     printf("Enter the value for n(nth bit):");
     scanf("%d", &n);
     input = input & (~0);
     printf("Result: %d\n", input);


}
  int flip(int input,int n)

{
     input = input ^ (1 << n);
     return input;
  }

//   int query()
// {
//   int n, input;
//      printf("Enter your input value:");
//      scanf("%d", &input);
//      printf("Enter the value for n(nth bit):");
//      scanf("%d", &n);



// }
 
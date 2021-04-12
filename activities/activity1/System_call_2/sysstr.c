#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
  printf("hello world");
  int ret;
  char rev[100];
  ret = syscall(398, "Abhishek Guria", rev);
  printf("\n Reverse back string is  %s\n", rev);
  if (ret < 0)
    perror("It works");
  return 0;
}


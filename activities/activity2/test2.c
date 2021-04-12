#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
  printf("hello world");
  int ret;
  ret = syscall(398);
  printf("\nreversed string is %d\n", ret);
  if (ret < 0)
    perror("testcall");
  return 0;
}
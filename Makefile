


Src = test/test.c\
src/bitmask.c\
src/mystring.c\
src/myutils.c


built: $(Src)
	gcc -Iinclude $(Src) -o output.exe
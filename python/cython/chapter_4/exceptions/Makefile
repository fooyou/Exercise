all:
	cython -2 cycode.pyx
	gcc -g -O2 -c cycode.c -o cycode.o `python-config --includes`
	gcc -g -O2 -c main.c -o main.o `python-config --includes`
	gcc -g -O2 -o example cycode.o main.o `python-config --libs`

clean:
	rm -f *.o example cycode.{h,c}

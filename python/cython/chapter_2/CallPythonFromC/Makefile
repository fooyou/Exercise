all:
	cython publicTest.pyx
	gcc -g -O2 -fpic -c publicTest.c -o publicTest.o `python-config --includes`
	gcc -g -O2 -fpic -c main.c -o main.o `python-config --include`
	gcc -g -O2 -o publicTest publicTest.o main.o `python-config --libs`

clean:
	rm -rf publicTest publicTest.c publicTest.h *.o

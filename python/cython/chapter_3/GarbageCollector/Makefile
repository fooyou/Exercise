all:
	cython -2 PyData.pyx PyData.pxd
	gcc -g -O2 -fPIC -c PyData.c -o PyData.o `python-config --includes`
	gcc -g -O2 -shared -o PyData.so PyData.o `python-config --libs`

clean:
	rm -f *.o *.so PyData.c


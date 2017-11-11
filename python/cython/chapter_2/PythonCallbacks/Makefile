all:
	cython -2 Callback.pyx
	gcc -g -O2 -Wall -c Callback.c -o Callback.o `python-config --includes`
	gcc -g -O2 -Wall -c main.c -o main.o `python-config --includes`
	gcc -o callback main.o Callback.o `python-config --libs`

clean:
	rm -rf *.o  callback Callback.{h,c}

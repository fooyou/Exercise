all:
	cython -2 cycode.pyx --embed
	g++ -g -O2 -c cycode.c -o cycode.o `python-config --includes`
	g++ -g -O2 -o example cycode.o `python-config --libs`

clean:
	rm -f *.o example cycode.{h,c}


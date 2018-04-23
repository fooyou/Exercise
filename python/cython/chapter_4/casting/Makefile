all:
	cython -2 cycode.pyx --embed
	gcc -g -O2 cycode.c -o example `python-config --includes --libs`

clean:
	rm -f *.o example cycode.c

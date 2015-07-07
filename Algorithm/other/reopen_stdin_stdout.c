#include <stdio.h>		// 'stdin' and 'stdout'
#include <stdlib.h>		// exit() 
#include <memory.h>		// memset()

const int CST_MAX_BUFFER = 256;

int main()
{
	char pInput[CST_MAX_BUFFER];
	memset(pInput, 0, sizeof(char) * CST_MAX_BUFFER);
	if ( NULL == freopen("out.txt", "w", stdout) )
	{
		printf("error: can not reopen out.txt as stdout.\n");
		exit(-1);
	}

	if ( NULL == freopen("in.txt", "r", stdin) )
	{
		fclose(stdout);
		printf("error: can not reopen in.txt as stdin.\n");
		exit(-1);
	}

	while ( scanf("%s", &pInput) != EOF )
	{
		printf("%s", pInput);
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}
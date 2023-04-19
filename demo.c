#include <stdio.h>


#define MAX_SIZE 40
int main(void)
{
	char anna[MAX_SIZE];
	char nick[10] = "bin";
	char ven[10] = "ls";

	snprintf(anna, MAX_SIZE, "/%s/%s", nick, ven);

	printf("%s\n", anna);

	return (0);
}


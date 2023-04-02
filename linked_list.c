#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*Defining structure*/

typedef struct list_s
{
	char *str;
	unsigned int len;
	struct list_s *next;

} list_t;

int main(void)
{
	/*Node declaration*/

	list_t *node1, *node2, *node3, *head, *current;

	/*Node memory allocation*/

	node1 = malloc(sizeof(list_t));
	node2 = malloc(sizeof(list_t));
	node3 = malloc(sizeof(list_t));

	/*Assigning value to the node*/

	node1->str = strdup("Amani");
	node1->len = 4;
	node2->str = strdup("Willian");
	node2->len = 7;
	node3->str = strdup("Nick");
	node3->len = 4;

	/*Assigning node addresses*/

	node1->next = node2;
	node2->next = node3;
	node3->next = NULL;

	/*Create head*/
	head = node1;

	/*Printing the list*/

	current = head;
	while (current != NULL)
	{
		printf("[%d] %s\n", current->len, current->str);
		free(current->str);
		current = current->next;
	}

	/*Freeing node memory*/

	current = head;
	while (current != NULL)
	{
		list_t *next = current->next;
		free(current);
		current = next;
	}
	return (0);
}

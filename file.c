#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*Structure definition*/

typedef struct list
{
	char *str;
	unsigned int len;
	struct list *next;
} list_t;



list_t insert_at_begin(list_t **head, const char *add)
{
	char *dup_add;
	/*Create new node*/

	/*Node declaration*/

	list_t *new;

	/*Memory allocation*/

	new = malloc(sizeof(list_t));
	
	/*Node initialization*/

	dup_add = strdup(add);
	new->str = dup_add;
	new->len = strlen(new->str);

	/*Node address*/

	new->next = *head;

	/*Create head*/
	*head = new;
}



int main(void)
{
	list_t *current;
	/*Node Declaration*/

	list_t *node1, *node2, *node3, *head;

	/*Memory Allocation*/

	node1 = malloc(sizeof(list_t));
	if (node1 == NULL)
		return (-1);
	node2 = malloc(sizeof(list_t));
	if (node2 == NULL)
		return (-1);
	node3 = malloc(sizeof(list_t));
	if (node3 == NULL)
		return (-1);

	/*Node initialization*/

	node1->str = strdup("Amani");
	node1->len = strlen(node1->str);
	node2->str = strdup("Willian");
	node2->len = strlen(node2->str);
	node3->str = strdup("Nick");
	node3->len = strlen(node3->str);

	/*Node address*/

	node1->next = node2;
	node2->next = node3;
	node3->next = NULL;

	/*Create the head*/

	head = node1;

	/*Call function*/

	insert_at_begin(&head, "Messi");

	/*Printing*/

	current = head;

	while (current != NULL)
	{
		printf("[%d] %s\n", current->len, current->str);
		free(current->str);
		current = current->next;
	}

	/*Freeing memory*/

	current = head;
	while (current != NULL)
	{
		struct list *next = current->next;

		free(current);
		current = next;
	}

	return (0);
}

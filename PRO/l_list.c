#include "alx.h"

/**
 * builtins_list - search for match and execute the associate builtin
 * @nick: struct for the program's data
 * Return: Returns the return of the function executed is there is a match,
 * otherwise returns -1.
 **/
int builtins_list(_st *nick)
{
	int iterator;
	builtins options[] = {
		{"exit", builtin_exit},
		{"help", builtin_help},
		{"cd", builtin_cd},
		{"alias", builtin_alias},
		{"env", builtin_env},
		{"setenv", builtin_set_env},
		{"unsetenv", builtin_unset_env},
		{NULL, NULL}
	};

/*walk through the structure*/
	for (iterator = 0; options[iterator].builtin != NULL; iterator++)
	{
/*if there is a match between the given command and a builtin,*/
		if (str_compare(options[iterator].builtin, nick->c, 0))
		{
/*execute the function, and return the return value of the function*/
			return (options[iterator].function(nick));
		}
/*if there is no match return -1 */
	}
	return (-1);
}

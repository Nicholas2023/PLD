#ifndef ALX_H
#define ALX_H

/**
 * Authour: Nick and Ann
 * File drp: Contains macros, func prototypes and structers
 */


/*File inclusion*/

#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <errno.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <signal.h>
#include <fcntl.h>
#include <stdio.h>



#define COMMAND_PROMPT "#KIMBA_REBEL$ "

#define UN_USED

#define B_SIZ 1024

/* Help information display macros */

#define CD_HELP_INFO "cd=\n"\
"cd: cd [dir]"\
"\n\tChange the pwd"\
"\n\tNULL arguments to be treated as cd HOME"\
"\n\tif argument is \"-\", the command changes the pwd"\
"\n\tto previous pwd"

#define EXIT_HELP_INFO "exit=\n"\
"exit: exit [STATUS]"\
"\n\tQuit the shell with a specified status code"\
"\n\tIf no status code is provided, the exit status code"\
"\n\twill be the same as that of the last executed command"

#define ENVIRONMENT_HELP_INFO "env=\n"\
"env: env"\
"\n\tDisplay a complete list of environment variables"\
"\n\tthat are currently set"

#define SETENV_HELP_INFO "setenv=\n"\
"setenv: setenv [VARIABLE VALUE]"\
"\n\tAdd or modify an environment variable"\
"\n\tIf an incorrect number of arguments is provided"\
"\n\tan error message will be displayed"

#define UNSETENV_HELP_INFO "unsetenv=\n"\
"unsetenv: unsetenv [VARIABLE]"\
"\n\tRemove an environment variable"\
"\n\tIf an incorrect number of arguments is provided,"\
"\n\tan error message will be displayed."

#define HELP_INFO_SEARCH "help=\n"\
"help: help [BUILTIN_CMD]"\
"\n\tDisplay information about built-in commands"\
"\n\tIf a specific command name is provided as an argument"\
"\n\tdetailed help for that command will be displayed"\
"\n\tIf no argument is provided, a list of available built-in commands will be displayed"\

/* include structures */

#include "data_handling.h"



/************* MAIN FUNCTIONS *************/


/*========  shell.c  ========*/

/* Inicialize the struct with the info of the program */
void inicialize_data(_st *nick, int arc, char *argv[], char **env);

/* Makes the infinite loop that shows the prompt*/
void sisifo(char *prompt, _st *nick);

/* Print the prompt in a new line */
void handle_ctrl_c(int opr UN_USED);


/*========  _getline.c  ========*/

/* Read one line of the standar input*/
int _getline(_st *nick);

/* split the each line for the logical operators if it exist */
int check_logic_ops(char *array_commands[], int i, char array_operators[]);


/*======== expansions.c ========*/

/* expand variables */
void expand_variables(_st *nick);

/* expand aliases */
void expand_alias(_st *nick);

/* append the string to the end of the buffer*/
int buffer_add(char *buffer, char *str_to_add);


/*======== str_tok.c ========*/

/* Separate the string in tokens using a designed delimiter */
void tokenize(_st *nick);

/* Creates a pointer to a part of a string */
char *_strtok(char *line, char *delim);


/*======== execute.c ========*/

/* Execute a command with its entire path */
int execute(_st *nick);


/*======== builtins_list.c ========*/

/* If match a builtin, executes it */
int builtins_list(_st *nick);


/*======== find_in_path.c ========*/

/* Creates an array of the path directories */
char **tokenize_path(_st *nick);

/* Search for program in path */
int find_program(_st *nick);


/************** HELPERS FOR MEMORY MANAGEMENT **************/


/*======== helpers_free.c ========*/

/* Frees the memory for directories */
void free_array_of_pointers(char **directories);

/* Free the fields needed each loop */
void free_recurrent_data(_st *nick);

/* Free all field of the data */
void free_all_data(_st *nick);


/************** BUILTINS **************/


/*======== builtins_more.c ========*/

/* Close the shell */
int builtin_exit(_st *nick;

/* Change the current directory */
int builtin_cd(_st *nick);

/* set the work directory */
int set_work_directory(_st *nick, char *new_dir);

/* show help information */
int builtin_help(_st *nick);

/* set, unset and show alias */
int builtin_alias(_st *nick);


/*======== builtins_env.c ========*/

/* Shows the environment where the shell runs */
int builtin_env(_st *nick);

/* create or override a variable of environment */
int builtin_set_env(_st *nick);

/* delete a variable of environment */
int builtin_unset_env(_st *nick);


/************** HELPERS FOR ENVIRONMENT VARIABLES MANAGEMENT **************/


/*======== env_management.c ========*/

/* Gets the value of an environment variable */
char *env_get_key(char *name, _st *nick);

/* Overwrite the value of the environment variable */
int env_set_key(char *key, char *value, _st *nick);

/* Remove a key from the environment */
int env_remove_key(char *key, _st *nick);

/* prints the current environ */
void print_environ(_st *nick);


/************** HELPERS FOR PRINTING **************/


/*======== helpers_print.c ========*/

/* Prints a string in the standar output */
int _print(char *string);

/* Prints a string in the standar error */
int _printe(char *string);

/* Prints a string in the standar error */
int _print_error(int errorcode, _st *nick);


/************** HELPERS FOR STRINGS MANAGEMENT **************/


/*======== helpers_string.c ========*/

/* Counts the number of characters of a string */
int str_length(char *string);

/* Duplicates an string */
char *str_duplicate(char *string);

/* Compares two strings */
int str_compare(char *string1, char *string2, int number);

/* Concatenates two strings */
char *str_concat(char *string1, char *string2);

/* Reverse a string */
void str_reverse(char *string);


/*======== helpers_numbers.c ========*/

/* Cast from int to string */
void long_to_string(long number, char *string, int base);

/* convert an string in to a number */
int _atoi(char *s);

/* count the coincidences of character in string */
int count_characters(char *string, char *character);


/*======== alias_management.c ========*/

/* print the list of alias */
int print_alias(_st *nick, char *alias);

/* get the alias name */
char *get_alias(_st *nick, char *alias);

/* set the alias name */
int set_alias(char *alias_string, _st *nick);

#endif /* ALX_H */

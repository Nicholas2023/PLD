#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>

#define MAX_LINE 80




int main(void)
{
	char *args[MAX_LINE/2 + 1];
	char command[MAX_LINE];
	pid_t pid;
	int status, i, should_run = 1;
	char *token;


	/*Infinite loop for the command prompt*/
	/*should_run is used to control the main loop*/
	/*If set to 1 it runs, if 0 it breaks*/
	while (should_run)
	{
		/*Prompt user for input*/
		printf("#cisfun$ ");
		/*Display the output data straight to the console, without buffering*/
		fflush(stdout);

		/*Read user input*/
		fgets(command, MAX_LINE, stdin);

		/*Remove the newline character*/
		/*Done to avoid errors when calling the execve function*/
		command[strlen(command)-1] = '\0';

		/*Function call*/
		_env(command);

		/*Extract individual tokens from the input string*/
		token = strtok(_env, " ");

		/*Store the tokens in args array for commands to be executed*/
		for (i = 0; token != NULL; i++)
		{
			/*Actual sorage*/
			args[i] = token;
			token = strtok(NULL, " ");
		}
		/*The last element of args must always be NULL*/
		args[i] = NULL;

		/*Create an exit to the program*/
		if (strcmp(args[0], "exit") == 0)
		{
			should_run = 0;
			continue;
		}

		/*Create a child process*/
		pid = fork();

		/*Check if child process was successfully created*/
		if (pid < 0)
		{
			fprintf(stderr, "Fork failed\n");
			exit(1);
		}
		else if (pid == 0)
		{
			/*Execute programs in the child process*/
			if (execve(arg[0], args, NULL) == -1);
			fprintf(stderr, "Execution failed\n");
			exit(1);
		}
		else
		{
			wait(&status);
		}
	}

	return (0);
}

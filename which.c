#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/*Define constants for max path and filename length*/
#define MAX_PATH_LENGTH 1024
#define MAX_FILENAME_LENGTH 256
#define MAX_LINE 80

int env(char *argv)
{
	/*Variable declaration*/
	char *path, path_copy[MAX_PATH_LENGTH], *dir, *filename;
	char filepath[MAX_PATH_LENGTH + MAX_FILENAME_LENGTH +1];

	/*Get the PATH environment variable*/
	path = getenv("PATH");

	/*Copy the PATH string to a buffer*/
	strncpy(path_copy, path, MAX_PATH_LENGTH -1);

	/*Make sure the buffer is null terminated*/
	path_copy[MAX_PATH_LENGTH - 1] = '\0';

	/*Get the filename to search for from the program arguments*/
	filename = argv;

	/*Split the PATH string into directories using ':' as a delimiter*/
	dir = strtok(path_copy, ":");

	/*Loop through each directory in the PATH*/

	while (dir)
	{
		/*Create the full file path by concatenating the directory and filename*/
		snprintf(filepath, MAX_PATH_LENGTH + MAX_FILENAME_LENGTH, "%s/%s", dir, filename);
		/*Check if the file exists at this path*/
		if (access(filepath, X_OK) == 0)
			return (0)

		/*Get the next directory in the PATH*/
		dir = strtok(NULL, ":");
	}
	/*If the file was not found in the PATH, print an error message and exit with status 1*/
	fprintf(stderr, "%s not found in PATH\n", filename);

	return (1);
}


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
		/*Display the output data staight to the console, without buffering*/
		fflush(stdout);

		/*Read user input*/
		fgets(command, MAX_LINE, stdin);

		/*Remove the newline character*/
		/*Done to avoid errors when calling the execve function*/
		command[strlen(command)-1] = '\0';

		/*Extract individual tokens from the input string*/
		token = strtok(command, " ");

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
			if (execve(args[0], args, NULL) == -1);
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

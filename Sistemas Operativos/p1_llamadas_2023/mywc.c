//P1-SSOO-22/23

#include <stdio.h>
#include <fcntl.h> // library for open system call 
#include <sys/types.h> 
#include <sys/stat.h> 
#include <unistd.h> // library for read system call

#define BUFFERSIZE 1

int main(int argc, char *argv[])
{

	//If less than two arguments (argv[0] -> program, argv[1] -> file to process) print an error y return -1
	if (argc < 2)
	{
		printf("Too few arguments\n");
		return -1;
	}

	char buffer[BUFFERSIZE];

	int file = open(argv[1], O_RDONLY);
	if (file < 0) {
		printf("mywc: %s: No such file or directory\n", argv[1]);
		return -1;
	}
	int n;
	// counters
	int bytes = 0;
	int words = 0;
	int lines = 0;
	int palabra = 1; // boolean. if 1, the next letter starts a new word
	while ((n = read(file, buffer, 1)) > 0) {
		++bytes;
		
		if (palabra && buffer[0] != ' ' && buffer[0] != '\t' && buffer[0] != '\n') { // new word
			palabra = 0; // not new word possible until it reads an space, tab o newline
			++words;
		} else if (buffer[0] == '\n') { // new line
			++lines;
			palabra = 1;
		} else if (buffer[0] == ' ' || buffer[0] == '\t') { // space or tab
			palabra = 1;
		}
	}

	close(file);
	printf("%d %d %d %s\n", lines, words, bytes, argv[1]); // output

	return 0;
}

//P1-SSOO-22/23

#include <stdio.h> //library for printf
#include <fcntl.h> // library for open system call 
#include <sys/types.h> 
#include <sys/stat.h> 
#include <unistd.h> // library for read and write system call
#include <string.h> 

#define BUFFERSIZE 1


int main(int argc, char *argv[])
{

    /* If less than two arguments (argv[0] -> program, argv[1] -> file to save environment) print an error y return -1 */
    if (argc < 3) {
    	printf("Too few arguments\n");
    	return -1;
    }

    int env = open("env.txt", O_RDONLY); // opens the file
    int out_file = open(argv[2], O_CREAT | O_TRUNC | O_WRONLY, 0755); // creates or replaces the output file

    if (env < 0 ) { // error oppening env.txt
		printf("myenv: error trying to open env\n");
		return -1;
	}
    
    if (out_file < 0) { // error creating out_file
		printf("myenv:error trying to create %s\n", argv[2]);
		return -1;
	}

    int len = strlen(argv[1]); 
    char buff[BUFFERSIZE];
    int possible_found = 1; // boolean. Indicates if it is possible to find the variable in the current reading line
    int n = 1; // bytes readed in the current iteration
    int index = 0; // controls which char of the variable must be compared 
    

    while (n > 0) {
        
        n = read(env, buff, 1);

        if (index == len ) { // instance of the variable
            if (buff[0] == '=') { // its the variable 
                 
                write(out_file, argv[1], len);
                while (n > 0 && buff[0] != '\n') { // copy the line 
                    write(out_file, buff, 1);
                    n = read(env, buff, 1);
                }
                if (n > 0) write(out_file, buff, 1); // new line in case the variable appears more than once

            } else {
                possible_found = 0;
            }
            
        }

        if (possible_found && buff[0] == argv[1][index]) { // compares if the character readed and the variable name are equal in the corresponding position
            ++index;
        } else {
            possible_found = 0; // if not, the variable is not in this line
            index = 0; // the next comparison must be done at the begining 
        }
        if (!possible_found) { // when starting a new line it is possible to find the variable
            if(buff[0] == '\n') {
                possible_found = 1;
            }
        }
    }
    close(out_file); // close file 
    close(env); // clos env
    return 0;
}

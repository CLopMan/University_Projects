//P1-SSOO-22/23

#include <stdio.h>		// Header file for system call printf
#include <unistd.h>		// Header file for system call gtcwd
#include <sys/types.h>	// Header file for system calls opendir, readdir y closedir
#include <dirent.h>
#include <string.h>

int main(int argc, char *argv[])
{
	char buff[PATH_MAX]; // PATH_MAX its a constant
	DIR* directorio; 
	if (argc > 1) {
		strcpy(buff, argv[1]); // with arguments
	} else {
		getcwd(buff, PATH_MAX); // with no arguments
	}
	directorio = opendir(buff); // opens dir 

	if (directorio == NULL) { // error oppening dir. It does not exist or general error. 
		printf("myls: error trying to open directory\n");
		return -1;
	}
	struct dirent* pdir; 
	while ((pdir = readdir(directorio))) { // reading loop
		printf("%s\n", pdir->d_name);
	}
	closedir(directorio); // close directory 
	return 0;
}


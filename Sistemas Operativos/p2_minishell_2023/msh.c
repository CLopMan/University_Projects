//P2-SSOO-22/23

// MSH main file
// Write your msh source code here

//#include "parser.h"
#include <stddef.h>         /* NULL */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <time.h>
#include <pthread.h>
#include <ctype.h> // preguntar

#define MAX_COMMANDS 8


// ficheros por si hay redirección
char filev[3][64];

//to store the execvp second parameter
char *argv_execvp[8];

// contador de comandos en bg
int count_bg = 0;

void siginthandler(int param)
{
	
	kill(-2, SIGKILL); // matar a los procesos que queden ejecutando en el momento de cerrar la terminal
		if (count_bg > 0) { // si quedan procesos zombies, se eliminan. Por si hubiera error en el wait,
							// se contempla la posibilidad de que no se puedan esperar a todos
				while (waitpid(-1, NULL, WNOHANG) > 0){
					count_bg--;
				}
			}
	printf("****  Saliendo del MSH **** \n");
	
	//signal(SIGINT, siginthandler);
	exit(0);
}


/* Timer */
pthread_t timer_thread;
unsigned long  mytime = 0;

void* timer_run ( )
{
	while (1)
	{
		usleep(1000);
		mytime++;
	}
}

/**
 * Get the command with its parameters for execvp
 * Execute this instruction before run an execvp to obtain the complete command
 * @param argvv
 * @param num_command
 * @return
 */
void getCompleteCommand(char*** argvv, int num_command) {
	//reset first
	for(int j = 0; j < 8; j++)
		argv_execvp[j] = NULL;

	int i = 0;
	for ( i = 0; argvv[num_command][i] != NULL; i++)
		argv_execvp[i] = argvv[num_command][i];
}


/**
 * Main sheell  Loop  
 */

int get_len(int n) {
	/*This function recieves an integer and returns the number of digits it has
	Esta función recibe un entero y devuelve el número de cifras que tiene*/
	int i = 0;
	if (n < 0) {
		n *= -1;
	}
	if (n == 0) {
		return 1;
	}
	while (n > 0) {
		n /= 10;
		++i;
	}
	return i;
}

int mytime_cm(char*** argvv, int command_counter, int bg) {
	/*función mytime del enunciado*/
	if (argvv[0][1] != NULL || command_counter > 1 || bg) { // comprobación de la correcta sintaxis
		printf("sintaxis incorrecta: mytime\n");
		return -1;
	} else if (strcmp(filev[0], "0") != 0 || strcmp(filev[1], "0") != 0 || strcmp(filev[2], "0") != 0) { // redirecciones 
		printf("sintaxis incorrecta: mytime\n");
		return -1;
	} else {
		// ejecución de mytime
		int aux = mytime;
		int horas = mytime / 3600000;
		aux -= 3600000 * horas;
		int min = aux / 60000;
		aux -= min*60000;
		int seg = aux / 1000;
		fprintf(stderr, "%.2d:%.2d:%.2d\n",horas, min, seg); // imprimir con formato. salida de error
		return 0;
	}
}

int mycalc_cm(char*** argvv, int command_counter, int bg) {
	/*Comprobación de la sitaxis*/
	int check_input = 0;
	if (command_counter > 1 || argvv[0][1] == NULL || argvv[0][2] == NULL || argvv[0][3] == NULL || argvv[0][4] != NULL || bg) { // argumentos necesarios

		check_input = 1;
	
	} else if (strcmp(filev[0], "0") != 0 || strcmp(filev[1], "0") != 0 || strcmp(filev[2], "0") != 0) { // redirecciones 
		check_input = 1;
	} else if (strcmp(argvv[0][2], "mul") != 0 && strcmp(argvv[0][2], "add") != 0 && strcmp(argvv[0][2], "div") != 0) { // operación reconocida

		check_input = 1;
	} else { // los operandos son enteros
		if ((argvv[0][1][0] != '-' && !isdigit(argvv[0][1][0])) || (argvv[0][3][0] != '-' && !isdigit(argvv[0][3][0]))) {
			check_input = 1;
		}
		for (int y = 1; y < strlen(argvv[0][1]); ++y) {
			if (isdigit(argvv[0][1][y]) == 0) {

				check_input = 1;
				break;
			}
		}
		for (int y = 1; y < strlen(argvv[0][3]); ++y) {
			if (isdigit(argvv[0][3][y]) == 0) {

				check_input = 1;
				break;
			}
		}

	}
	if (check_input) { // parámetros incorrectos 
		printf("[ERROR] La estructura del comando es mycalc <operando_1> <add/mul/div> <operando_2>\n");
		return -1;
	} else {
		int acc = atoi(getenv("Acc")); // variable de entorno
		int acc_len; // número de cifras de la variable (se usa más tarde)
		char* acc_str; // buffer para la conversión de int -> str
		int result; // resultado de las operaciones 
		int resto; // resto de la división
		int op1 = atoi(argvv[0][1]), op2 = atoi(argvv[0][3]); // operandos 

		if (strcmp(argvv[0][2], "add") == 0) { // SUMA 
			result = op1 + op2;
			acc += result;
			acc_len = get_len(acc); // número de cifras de acc
			acc_str = (char*) malloc(acc_len + 2); // +2: '-' and '\0'
			sprintf(acc_str, "%i", acc); // int -> str
			setenv("Acc", acc_str, 1); // actualiza la variable de entorno con sobreescritura 
			fprintf(stderr, "[OK] %d + %d = %d; Acc %i\n", op1, op2, result, acc);
			free(acc_str);

		} else if (strcmp(argvv[0][2], "mul") == 0) { // producto
			result = op1 * op2;
			fprintf(stderr, "[OK] %d * %d = %d\n", op1, op2, result);
		
		} else { // cociente
			if (op2 == 0) {
				printf("[ERROR] division entre 0\n");
				return 1;
			} else {
				result = op1 / op2;
				resto = op1 - op2*result;
				fprintf(stderr, "[OK] %d / %d = %d; Resto %d\n", op1, op2, result, resto);
			}
			
		}
		return 0;
	}
	
}

int main(int argc, char* argv[])
{
	/**** Do not delete this code.****/
	int end = 0; 
	int executed_cmd_lines = -1;
	char *cmd_line = NULL;
	char *cmd_lines[10];

	if (!isatty(STDIN_FILENO)) {
		cmd_line = (char*)malloc(100);
		while (scanf(" %[^\n]", cmd_line) != EOF){
			if(strlen(cmd_line) <= 0) return 0;
			cmd_lines[end] = (char*)malloc(strlen(cmd_line)+1);
			strcpy(cmd_lines[end], cmd_line);
			end++;
			fflush (stdin);
			fflush(stdout);
		}
	}

	pthread_create(&timer_thread,NULL,timer_run, NULL);

	/*********************************/

	char ***argvv = NULL;
	int num_commands;

	setenv("Acc", "0", 1);
	while (1) 
	{
		int status = 0;
		int command_counter = 0;
		int in_background = 0;
		signal(SIGINT, siginthandler);

		// Prompt 
		write(STDERR_FILENO, "MSH>>", strlen("MSH>>"));

		// Get command
		//********** DO NOT MODIFY THIS PART. IT DISTINGUISH BETWEEN NORMAL/CORRECTION MODE***************
		executed_cmd_lines++;
		if( end != 0 && executed_cmd_lines < end) {
			command_counter = read_command_correction(&argvv, filev, &in_background, cmd_lines[executed_cmd_lines]);
		}
		else if( end != 0 && executed_cmd_lines == end){
			return 0;
		}
		else{
			command_counter = read_command(&argvv, filev, &in_background); //NORMAL MODE
		}
		//************************************************************************************************


		/************************ STUDENTS CODE ********************************/
		int end_status; // variable para recoger el estado de terminación del hijo
		if (command_counter > 0) {
			if (command_counter > MAX_COMMANDS){
				printf("Error: Numero máximo de comandos es %d \n", MAX_COMMANDS);
			}
			else {
				/*mandatos internos*/
				if(strcmp(argvv[0][0], "mytime") == 0) { 
					mytime_cm(argvv, command_counter, in_background);
					
					
				} else if (strcmp(argvv[0][0], "mycalc") == 0){
					mycalc_cm(argvv, command_counter, in_background);
					
					
				} else {
					/*mandatos externos*/
					int pids[MAX_COMMANDS]; // almacén de pids
					int pipes[MAX_COMMANDS - 1][2]; // tendremos a lo sumo 7 tuberías
					int error_out = -1, input_file = -1, output_file = -1, redic_ctrl = 1;

					if (command_counter > 1) {
						/* Creación de pipes*/
						for (int x = 0; x < command_counter - 1; ++x) {
							if (pipe(pipes[x]) < 0){
								perror("Error creacion de tuberias");
								redic_ctrl = 0;
							}
						}
					}
					if (strcmp(filev[2], "0") != 0) {
						 // redirección de error 
						if ((error_out = open(filev[2], O_CREAT|O_TRUNC|O_WRONLY, 0666)) < 0) {
							perror("OPEN error_out");
							redic_ctrl = 0;
						}
					}
					if (strcmp(filev[0], "0") != 0) {
						// redirección de entrada
						if ((input_file = open(filev[0], O_RDONLY)) < 0) {
							perror("OPEN input_file");
							redic_ctrl = 0;
						}
					}

					if (strcmp(filev[1], "0") != 0) {
						// redirección de salida
						if ((output_file = open(filev[1], O_WRONLY|O_CREAT|O_TRUNC, 0666)) < 0) {
							perror("OPEN output_file");
							redic_ctrl = 0;
						}
					}
					if (redic_ctrl) { // solo se ejecuta el mandato si no ha habido errores de redirección o tuberías 
						for (int x = 0; x < command_counter; ++x) {
							pids[x] = fork();
							if (pids[x] == 0) {
								// salida de errores, para todos los hijos
								if (error_out >= 0) {
									if (close(STDERR_FILENO) < 0){
										perror("error close stderr");
										exit(-1);
									}
									if (dup(error_out) < 0){
										perror("error dup error_out");
										exit(-1);
									}
									if (close(error_out) < 0){
										perror("error close error_out");
										exit(-1);
									}
									
								}
								if (x == 0) {
									// redireccion de entrada para el primer hijo
									if (input_file >= 0) {
										if (close(STDIN_FILENO < 0)){
											perror("error close stdin");
											exit(-1);
										}
										if (dup(input_file) < 0){
											perror("error dup input_file");
											exit(-1);
										}
										if (close(input_file) < 0){
											perror("error close input_file");
											exit(-1);
										}
									}
								}
								if (x == command_counter - 1) {
									// redireccion de salida para el ultino hijo
									if (output_file >= 0) {
										if (close(STDOUT_FILENO) < 0){
											perror("error close stdout");
											exit(-1);
										}
										if (dup(output_file) < 0){
											perror("error dup output_file");
											exit(-1);
										}
										if (close(output_file) < 0){
											perror("error close output_file");
											exit(-1);
										}
									}
								}
								// gestión de pipes
								for (int p = 0; p < command_counter - 1; ++p) {
									if (p == x - 1) {
										//tuberia de lectura
										if (dup2(pipes[p][0], STDIN_FILENO) < 0){
											perror("error pipes");
											exit(-1);
										}
									} else if (p == x) {
										//tuberia de escritura
										if (dup2(pipes[p][1], STDOUT_FILENO) < 0){
											perror("error pipes");
											exit(-1);
										}
									}
									// cerramos las tuberías 
									if (close(pipes[p][0]) < 0){
											perror("error pipes");
											exit(-1);
										}
									if (close(pipes[p][1]) < 0){
											perror("error pipes");
											exit(-1);
										}
									
									
								}
								// cambio de imagen
								execvp(argvv[x][0], &argvv[x][0]);
								perror("execvp failed");
								exit(-1);
							}

						}

						//cerramos las tuberías para el padre 
						for (int p = 0; p < command_counter - 1; ++p) {
							if (close(pipes[p][0]) < 0){
									perror("error pipes");
									exit(-1);
								}
							if (close(pipes[p][1]) < 0){
									perror("error pipes");
									exit(-1);
								}
						}

						// espera de los hijos NO en background
						if (!in_background) {
							for (int x = 0; x < command_counter; ++x) {
								//printf("pid killed: %i \n", pids[x]);
								if (waitpid(pids[x], &end_status, 0) < 0){
									fprintf(stderr,"Error funcionamiento de wait\n");
								}
								if (end_status != 0) { // en caso de errores de ejecución
									fprintf(stderr,"Error de ejecución\n");
								}
							}

						} else { // hijos en background 
							printf("[%d]\n", pids[command_counter -1]);
							count_bg += command_counter;

						}
					}
					
					// para cada ciclo de la minishell, si hay hijos en background que hayan terminado, los esperamos.
					if (count_bg > 0) {
						while (waitpid(-1, &end_status, WNOHANG) > 0){
							count_bg--;
							if (end_status != 0) {
								perror("Error de ejecución");
							}
						}
					}
					//Close de los descriptores en el padre

					if (error_out >= 0) {
						if (close(error_out) < 0){
							perror("error close error_out");
						}
					}
					if (input_file >= 0) {
						if (close(input_file) < 0){
							perror("error close input_file");
						}
					}
					if (output_file >= 0) {
						if (close(output_file) < 0){
							perror("error close output_file");
						}
					}
				}
					
			}
		}
	}
	
	return 0;
}
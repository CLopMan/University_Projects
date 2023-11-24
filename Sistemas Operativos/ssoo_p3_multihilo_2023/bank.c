// SSOO-P3 2022-2023

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stddef.h>
#include <sys/stat.h>
#include <pthread.h>
#include "queue.h"
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

/*Cuando se hace un return en el main se liberarán los recursos de programa, aún así hacemos el free?
HAZ UN FREE ANTES DEL RETURN*/

/*****VARIABLES GLOBALES*****/
unsigned client_numop = 0; // numero de hilos_productores
unsigned bank_numop = 0;   // número de hilos_consumidores
int global_balance = 0;

struct element **list_client_ops; // array de operaciones
int* saldos;
queue *cola; // buffer circular
pthread_mutex_t becario; // mutex entre consumidores y productores
pthread_cond_t no_lleno; // condicion 
pthread_cond_t no_vacio; // condicion



/*****MÉTODOS OPERACIONES*****/
int read_op(FILE *file, struct element *op, int od, int n_maxcuentas) {
    if (fscanf(file, "%s", op->name) == EOF) {
        return 1;
    }
    // printf("operacion: %s\n", op->name);
    op->order = od;
    // printf("operation order: %i\n", op->order);
    if (strcmp(op->name, "CREAR") == 0 || strcmp(op->name, "SALDO") == 0)
    {
        fscanf(file, "%i", &op->arg[0]);
        op->arg[1] = 0;
        op->arg[2] = 0;
        if (op->arg[0] > n_maxcuentas) {
            perror("Numero de cuenta supera el maximo");
            return 2;
        }
    }
    else if (strcmp(op->name, "INGRESAR") == 0 || strcmp(op->name, "RETIRAR") == 0)
    {
        fscanf(file, "%i %i", &op->arg[0], &op->arg[1]);
        op->arg[2] = 0;
    }
    else if (strcmp(op->name, "TRASPASAR") == 0)
    {
        fscanf(file, "%i %i %i", &op->arg[0], &op->arg[1], &op->arg[2]);
    }
    else
    {
        perror("Operacion no existe");
    }
    return 0;
}

void print_op(struct element *op)
{
    printf("Operacion: %s\norden: %i\n", op->name, op->order);
    int i = 0;
    while (i < 3)
    {
        printf("%i\n", op->arg[i]);
        ++i;
    }
    printf("=====================\n");
}

void funcionoperaciones(struct element* op){
    if (strcmp(op->name, "CREAR") == 0) {
        saldos[op->arg[0] - 1] = 0;
        printf("%i %s %i SALDO=%i TOTAL=%i\n", op->order, op->name, op->arg[0], saldos[op->arg[0]- 1], global_balance);
    } else if (strcmp(op->name, "SALDO") == 0){
        printf("%i %s %i SALDO=%i TOTAL=%i\n", op->order, op->name, op->arg[0], saldos[op->arg[0]- 1], global_balance);
    } else if (strcmp(op->name, "INGRESAR") == 0) {
        saldos[op->arg[0] - 1] += op->arg[1];
        global_balance += op->arg[1];
        printf("%i %s %i %i SALDO=%i TOTAL=%i\n", op->order, op->name, op->arg[0], op->arg[1], saldos[op->arg[0]- 1], global_balance);
    } else if (strcmp(op->name, "RETIRAR") == 0) {
        saldos[op->arg[0] - 1] -= op->arg[1];
        global_balance -= op->arg[1];
        printf("%i %s %i %i SALDO=%i TOTAL=%i\n", op->order, op->name, op->arg[0], op->arg[1], saldos[op->arg[0]- 1], global_balance);
    } else if (strcmp(op->name, "TRASPASAR") == 0) {
        saldos[op->arg[0] - 1] -= op->arg[2];
        saldos[op->arg[1] - 1] += op->arg[2];
        printf("%i %s %i %i %i SALDO=%i TOTAL=%i\n", op->order, op->name, op->arg[0], op->arg[1], op->arg[2], saldos[op->arg[1]- 1], global_balance);
    }
}
/*****FIN MÉTODOS OPERACIONES*****/

/*****PRODUCTOR CONSUMIDOR*****/
void * productor(void* param)
{
    int* pn = (int*)param;
    while(1){
        printf("Productor intanta tomar el mutex\n");
        pthread_mutex_lock(&becario);
        printf("productor gana\n");
        while(queue_full(cola)){
            // condición de parada
            pthread_cond_wait(&no_lleno, &becario);
        }
        if (client_numop >= *pn) {
                pthread_mutex_unlock(&becario);
                pthread_cond_broadcast(&no_lleno);
                pthread_exit(0);
            }
        queue_put(cola, list_client_ops[client_numop]);
        ++client_numop;
        pthread_cond_broadcast(&no_vacio);
        pthread_mutex_unlock(&becario);
    }
}

void * consumidor(void* param)
{
    int* pn = (int*)param;
    while(1){
        printf("Consumidor intenta tomar el mutex\n");
        pthread_mutex_lock(&becario);
        printf("Consumidor gana:\n");
        while(queue_empty(cola)){
            //condicion de parada
            if (bank_numop >= *pn) {
                pthread_mutex_unlock(&becario);
                pthread_cond_broadcast(&no_vacio);
                pthread_exit(0);
            }
            pthread_cond_wait(&no_vacio, &becario); 
        }
        struct element *elemento = queue_get(cola);
        ++bank_numop;
        if(bank_numop != elemento->order){
            perror("Error en el orden de ejecucion");
        }
        //funcionoperaciones(elemento); //ejecucion e impresion(actualizar saldo de cuenta especifica y de global)
        free(elemento);
        pthread_cond_broadcast(&no_lleno);
        pthread_mutex_unlock(&becario);
    }
}
/*****FIN DEL PRODUCTOR CONSUMIDOR*****/

/*****MÉTODOS GENÉRICOS*****/
void liberar_recursos(pthread_t* cajero, pthread_t* trabajador) {
    free(cajero);
    free(trabajador);
    free(saldos);
    free(list_client_ops);
    queue_destroy(cola);
}



/**
 * Entry point
 * @param argc
 * @param argv
 * @return
 */
int main(int argc, const char *argv[]) {
    /*VALIDACIÓN DE ARGUMENTOS*/
    if (atoi(argv[2]) <= 0 || atoi(argv[3]) <= 0 || atoi(argv[4]) <= 0 || atoi(argv[5]) <= 0) {
        perror("Error en los argumentos");
        return -1;
    }

    /*VARIABLES LOCALES*/
    FILE *input_file;
    int n;         // número de operaciones que se van a procesar
    char n_str[5]; // 5 = 3 dígitos + '\n' + '\0'
    int n_maxcuentas = atoi(argv[4]); 
    int read_ctrl; // recoge la salida de la lectura de operación de fichero

    /*VARIABLES GLOBALES*/
    pthread_t* cajero = (pthread_t*)malloc(atoi(argv[2]) * sizeof(pthread_t));
    pthread_t* trabajador = (pthread_t*)malloc(atoi(argv[3]) * sizeof(pthread_t));
    saldos = (int*)malloc(n_maxcuentas*sizeof(int));
    cola = queue_init(atoi(argv[5])); // inicialización de la cola 


    /*LECTURA DEL FICHERO*/
    if ((input_file = fopen(argv[1], "r")) == NULL)
    {
        perror("fopen");
        liberar_recursos(cajero, trabajador);
        return -1;
    }
    fgets(n_str, 4, input_file);
    n = atoi(n_str);
    list_client_ops = (struct element **)malloc(n * sizeof(struct element*)); 
    if (n > 200)
    {
        perror("Excedido el numero de operaciones máximo (200)");
        liberar_recursos(cajero, trabajador);
        return -1;
    }

    for (int i = 0; i < n; ++i) {
        struct element *op;
        op = element_init();
        if ((read_ctrl = read_op(input_file, op, i + 1, n_maxcuentas)) == 1)
        {   
            for (int j = 0; j < i; j++ ) free(list_client_ops[j]); // liberación de los elementos creados hasta ese momento
            free(op);
            perror("Se han especificado más operaciones de las incluídas en el fichero");
            liberar_recursos(cajero, trabajador);
            return -1; 
        } else if (read_ctrl == 2) {
            for (int j = 0; j < i; j++ ) free(list_client_ops[j]); // liberación de los elementos creados hasta ese momento
            free(op);
            perror("Se intentó crear una cuenta que supera el índice máixmo");
            liberar_recursos(cajero, trabajador);
            return -1;
        }
        list_client_ops[i] = op;
    }
    // una lectura más por si hubiera más operaciones 
    struct element *op;
    op = element_init();

    if (read_op(input_file, op, -1, n_maxcuentas) != 1) {
        for (int j = 0; j < n; j++ ) free(list_client_ops[j]); // liberación de los elementos creados hasta ese momento
        perror("Se han especificado menos operaciones de las incluídas en el fichero");
        free(op); 
        liberar_recursos(cajero, trabajador);
        return -1; 
    }
    free(op); 
    fclose(input_file);
    /*FIN DE LECTURA DE FICHERO*/

    /*INICIALIZACIÓN DE MUTEX Y CREACIÓN DE HILOS*/
    pthread_mutex_init(&becario, NULL);
    pthread_cond_init(&no_lleno,NULL);
    pthread_cond_init(&no_vacio,NULL);

    for(int i = 0; i < atoi(argv[2]); ++i){
        pthread_create(&cajero[i], NULL, productor, (void*)&n);
    }
    for(int i = 0; i < atoi(argv[3]); ++i){
        pthread_create(&trabajador[i], NULL, consumidor, (void*)&n);
    }
    /*FIN DE CREACION DE HILOS*/
    
    /*ESPERA DE HILOS*/
    for(int i = 0; i < atoi(argv[2]); ++i){
        pthread_join(cajero[i], NULL);
    }
    for(int i = 0; i < atoi(argv[3]); ++i){
        pthread_join(trabajador[i], NULL);
    }
    /*FIN DE LA ESPERA DE HILOS*/
    
    /*LIBERACIÓN DE RECURSOS*/
    pthread_mutex_destroy(&becario);
    pthread_cond_destroy(&no_lleno);
    pthread_cond_destroy(&no_vacio);
    liberar_recursos(cajero, trabajador);
    return 0;
}
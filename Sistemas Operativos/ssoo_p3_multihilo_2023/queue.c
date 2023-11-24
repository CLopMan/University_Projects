// SSOO-P3 2022-2023

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include "queue.h"

struct element *element_init()
{

	struct element *pelem = (struct element *)malloc(sizeof(struct element));
	struct element elem;
	*pelem = elem;
	return pelem;
}

// To create a queue
queue *queue_init(int size)
{
	queue *q = (queue *)malloc(sizeof(queue));
	queue __queue;
	__queue.head = (struct element **)malloc(size * sizeof(struct element *));
	__queue.ins_index = 0;	 // primer indice libre donde insertar // posible eliminación de esto
	__queue.pop_index = 0;	 // primer indice lleno donde sacar elemento
	__queue.max_size = size; // tamaño del buffer circular (perímetro)
	__queue.size = 0;		 // numero de elementos almacenados
	*q = __queue;
	return q;
}

// To Enqueue an element
int queue_put(queue *q, struct element *x)
{
	if (queue_full(q))
	{
		printf("La cola está llena\n");
		return -1;
	}
	q->head[q->ins_index] = x;						 // se añade la operación en la posición libre
	q->ins_index = (q->ins_index + 1) % q->max_size; // se actualiza el indice de inserción, teniendo en cuenta su naturaleza circular
	++(q->size);
	return 0;
}

// To Dequeue an element.
struct element *queue_get(queue *q)
{
	if (queue_empty(q))
	{
		printf("la cola está vacía\n");
		return NULL;
	}
	struct element *element;
	element = q->head[q->pop_index];				 // acceso a la operación que deba borrarse primero
	q->head[q->pop_index] = NULL;					 // borrado de la posición
	q->pop_index = (q->pop_index + 1) % q->max_size; // se actualiza el indice de get, teniendo en cuenta su naturaleza circular
	--(q->size);
	return element;
}

// To check queue state
int queue_empty(queue *q)
{
	if (q->size == 0)
		return 1;
	return 0;
}

int queue_full(queue *q)
{
	if (q->size >= q->max_size)
		return 1;
	return 0;
}

// To destroy the queue and free the resources
int queue_destroy(queue *q)
{
	/*libera lo que está dentro*/
	if (!queue_empty(q))
	{
		for (int i = q->pop_index; i < q->ins_index; ++i)
		{
			if (q->head[i] != NULL)
				free(q->head[i]);
		}
	}

	/*libera la cola*/
	free(q->head);
	free(q);
	return 0;
}

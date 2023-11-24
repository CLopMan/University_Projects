#ifndef HEADER_FILE
#define HEADER_FILE

struct element
{
	// Define the struct yourself
	char name[10]; // nombre de la operacion
	int arg[3];	   // argumentos de la operacion
	int order;	   // ordinal entre operaciones
};

typedef struct queue
{
	// Define the struct yourself
	struct element** head;
	int max_size;
	int ins_index;
	int pop_index;
	int size;
} queue;
struct element* element_init();

queue *queue_init(int size);
int queue_destroy(queue *q);
int queue_put(queue *q, struct element *elem);
struct element *queue_get(queue *q);
int queue_empty(queue *q);
int queue_full(queue *q);

#endif

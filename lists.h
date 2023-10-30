#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 * struct list_a - singly linked list
 * @n: integer
 * @next: pointer to the next node
 */
typedef struct list_a
{
	int n;
	struct list_a *next;
} list_b;

size_t print_list(const list_b *s);
list_b *add_node(list_b **head, const int n);
void free_list(list_b *head);
int update_check(list_b *list);

#endif

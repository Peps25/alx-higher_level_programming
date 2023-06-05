#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - the singly linked list
 * @n: the int
 * @next: this will point to the next node
 *
 * description: singly linked list node structure
 * for Holberton project
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
}
listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);

#endif

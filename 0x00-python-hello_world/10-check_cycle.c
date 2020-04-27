#include "lists.h"

/**
 * check_cycle - list
 * @list:  type list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	listint_t *node = list->next;

	while (node != NULL && node != list)
		node = node->next;
	return (node == list);
	return (1);
}

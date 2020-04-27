#include "lists.h"
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

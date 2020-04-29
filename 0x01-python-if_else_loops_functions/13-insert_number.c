#include "lists.h"

/**
 * insert_node - funtion
 * @head: single list in
 * @number: data new
 * Return: number of elemt in the linked lis
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux;
	unsigned int i = 0;

	aux = *head;
	while (aux != NULL)
	{
		if (number < aux->n)
			return (insert_nodeint_at_index(head, i, number));

		i++;
		aux = aux->next;
	}
	return (insert_nodeint_at_index(head, i, number));
}

/**
 * insert_nodeint_at_index - insert new node in the index possition
 * @head: linked list
 * @idx: index, it start in 0
 * @n: data for new node
 * Return: Always addres new node
 */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	unsigned int i = 0;
	unsigned int size_list = idx;
	listint_t *aux = *head;
	listint_t *new_node = NULL;

	/* validate if list is diferent of NULL */
	if (head == NULL)
		return (NULL);

	/* create new node of the size the listint_t */
	new_node = (listint_t *)malloc(sizeof(listint_t));
	/* validate if the size of list and new_node is ok */
	if (new_node == NULL || idx > size_list)
	{
		free(new_node);
		return (NULL);
	}
	/* set data a new node */
	new_node->n = n;
	if (idx == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	/* find match betwin idx and i var */
	while (aux != NULL)
	{
		if (i == (idx - 1))
		{
			new_node->next = aux->next;
			aux->next = new_node;
			return (new_node);
		}
		aux = aux->next;
		i++;
	}
	return (NULL);
}

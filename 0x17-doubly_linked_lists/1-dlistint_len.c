#include "lists.h"

/**
 * dlistint_len - mesure the lenght of a doubly linked list.
 * @h: head of the list.
 * Return: the number of elements in a linked dlistint_t list.
 */
size_t dlistint_len(const dlistint_t *h)
{
	int i = 0;

	while (h)
	{
		h = h->next;
		i++;
	}
	return (i);
}

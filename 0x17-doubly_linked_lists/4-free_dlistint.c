#include "lists.h"

/**
 * free_dlistint - frees a dlistint_t list.
 * @head: head of the list.
 * Return: None
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp = NULL;

	while (head)
	{
		tmp = head->next;
		free(head);
		head = tmp;
	}
}


#include "lists.h"
/**
 * sum_dlistint - calculate the sum of all the data (n) of a
 * dlistint_t linked list.
 * @head: the head of the doubley linked list.
 * Return: the sum or 0 if the list is empty.
 */
int sum_dlistint(dlistint_t *head)
{
	int sum = 0;

	while (head)
	{
		sum += head->n;
		head = head->next;
	}
	return (sum);
}

#include "lists.h"
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n);
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index);
size_t listint_len(const listint_t *h);

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to a header of signly linked list.
 * @number: number to be added.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	unsigned int i = 0;
	listint_t *h = *head;

	while (h)
	{
		if (h->n > number)
			return (insert_nodeint_at_index(head, i, number));
		h = h->next;
		i++;
	}
	if (!h)
		return (insert_nodeint_at_index(head, i, number));
	return (NULL);
}

/**
 * insert_nodeint_at_index - inserts a new node at a given position..
 * @head: pointer to pointer of head of signly linked list.
 * @n: value to add as data to each node.
 * @idx: index of the list where the new node should be added.It starts at 0.
 * if it is not possible to add the new node at index idx,
 * do not add the new node and return NULL.
 *
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	listint_t *courant, *new, *prev;
	size_t last_idx;

	last_idx = listint_len(*head);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (idx == (unsigned int)last_idx && idx)
	{
		courant = get_nodeint_at_index(*head, idx - 1);
		courant->next = new;
		return (new);
	}
	else
	{
		/* if courant is null*/
		courant = get_nodeint_at_index(*head, idx);
		/*mean the function get,didn't find that node-not possible to add*/
		if (!courant)
			new->next = NULL;
		else
			new->next = courant;
		if (idx == 0)
			*head = new;
		else
		{
			prev = get_nodeint_at_index(*head, idx - 1);
			prev->next = new;
		}
		return (new);
	}
}


/**
 * get_nodeint_at_index - nth node of a listint_t linked list.
 * @head: pointer to a header of signly linked list.
 * @index: the index of the node, starting at 0.
 * Return:  returns the nth node, if the node does not exist, return NULL.
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int i = 0;
	listint_t *h = head;

	while (h)
	{
		if (index == i)
			return (h);
		h = h->next;
		i++;
	}
	return (NULL);
}
/**
 * listint_len - returns the number of elements in a linked listint_t list.
 * @h: pointer to a header of signly linked list.
 * Return: the number of elements.
 */
size_t listint_len(const listint_t *h)
{
	if (!h)
		return (0);
	else
		return (1 + listint_len(h->next));
}

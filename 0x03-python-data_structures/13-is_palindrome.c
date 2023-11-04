#include "lists.h"
listint_t *reverse_listint(listint_t **head);
size_t list_len(const listint_t *h);

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to struct-head.
 *
 * An empty list is considered a palindrome
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	size_t len = list_len(*head), i = 1, half = 0;
	listint_t *head_1 = *head, *h = *head, *head_2 = NULL, *h_2 = NULL;

	if (!len)
		return (1);
	half = len % 2 == 0 ? len / 2 : len / 2 + 1;
	/* split the linked list into 2 halfs */
	while (i < len)
	{
		h = h->next;
		i++;
		if (i == half)
		{
			head_2 = h->next;
			h->next = NULL;
			break;
		}
	}
	/* reverse the second half of the linked list */
	head_2 = reverse_listint(&head_2);
	h_2 = head_2;
	i = 0;
	/* compare the 1st and 2nd reversed half togather */
	half = len % 2 == 0 ? half : half - 1;
	while (i < half)
	{
		if (head_1->n != head_2->n)
		{
			head_2 = reverse_listint(&h_2);
			h->next = head_2;
			return (0);
		}
		head_1 = head_1->next;
		head_2 = head_2->next;
		i++;
	}
	head_2 = reverse_listint(&h_2);
	h->next = head_2;
	return (1);
}



/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: pointer to pointer to struct-head.
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *cur, *nex;

	if (!(*head))
		return (NULL);
	cur = (*head)->next;
	if (!(cur))
		return (*head);
	nex = cur->next;
	if (!nex)
	{
		(*head)->next = NULL;
		cur->next = (*head);
		*head = cur;
		return (*head);
	}
	(*head)->next = NULL;

	cur->next = (*head);
	while (nex)
	{
		*head = cur;
		cur = nex;
		nex = cur->next;
		cur->next = (*head);
		if (!nex)
			*head = cur;
	}
	return (*head);
}

/**
 * list_len - the number of elements in a linked list_t list.
 * @h: pointer to a struct of type list_t.
 * Return:  the number of elements.
 */
size_t list_len(const listint_t *h)
{
	size_t i = 0;

	while (h != NULL)
	{
		h = h->next;
		i++;
	}
	return (i);
}

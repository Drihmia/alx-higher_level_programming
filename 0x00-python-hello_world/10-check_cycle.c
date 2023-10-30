#include "lists.h"


/**
 * check_cycle - finds the loop in a linked list.
 * @list: pointer to a lister of signly linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *cur, *faster;

	if (!list)
		return (0);

	cur = list;
	faster = list;
	while (cur && faster && (faster->next))
	{
		cur = cur->next;
		faster = faster->next->next;
		if (faster == cur)
		{
			cur = list;
			while (cur != faster)
			{
				cur = cur->next;
				faster = faster->next;
			}
			return (1);
		}
	}
	return (0);
}

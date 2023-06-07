#include "lists.h"

/**
 * check_cycle – prototype for checking linked list with a cycle
 * @list: parameter for linked list
 * Return: 1 for list with cycle, 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}

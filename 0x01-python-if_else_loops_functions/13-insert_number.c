#include "lists.h"

/**
 * insert_node – prototype fns that inserts a number into a sorted singly-linked list.
 * @head: parameter variable for pointer
 * @number: parameter variable for number.
 * Return: NULL if fails Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	/*introducing parameter variable*/
	listint_t *node = *head, *retval;

	/*allocating value for retval on memory*/
	retval = malloc(sizeof(listint_t));

	/*introducing conditional statement*/
	if (retval == NULL)
		return (NULL);
	retval->n = number;

	if (node->n >= number || node == NULL)
	{
		retval->next = node;
		*head = retval;
		return (retval);
	}

	/*introducing loop statement*/
	while (node && node->next && node->next->n < number)
		node = node->next;

	retval->next = node->next;
	node->next = retval;

	return (retval);
}

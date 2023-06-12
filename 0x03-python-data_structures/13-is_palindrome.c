#include "lists.h"

/**
 * reverse_listint - function that reverses a listint_t linked list.
 * @head: parameter for pointer to the first node in the list
 * Return: parameter for pointer to the first node in the new list
 */
listint_t *reverse_listint(listint_t **head)
{
	/*introducing variable parameter*/
	listint_t *prev;
	listint_t *next;

	/*initializing variable parameter*/
	prev = NULL;
	next = NULL;

	/*conditional statement for the function*/
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - function returns 1 if a string is a palindrome and 0 if not.
 * @head: pointer parameter to the linked list head.
 * Return: 1 if it is, 0 it's not
 */
int is_palindrome(listint_t **head)
{
	/*introducing parameters for the function*/
	listint_t *q, *y, *z;
	size_t i, j;

	j = 0;
	/*conditional statement for the function*/
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	y = *head;
	while (y)
	{
		j++;
		y = y->next;
	}
	y = *head;
	for (i = 0; i < (j / 2) - 1; i++)
		y = y->next;
	if ((j % 2) == 0 && y->n != y->next->n)
		return (0);

	y = y->next->next;
	z = reverse_listint(&y);
	q = z;

	y = *head;
	while (z)
	{
		if (y->n != z->n)
			return (0);
		y = y->next;
		z = z->next;
	}
	reverse_listint(&q);

	return (1);
}

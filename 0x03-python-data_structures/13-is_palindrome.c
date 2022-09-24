#include "lists.h"

/**
 * is_palindrome - checks if a list is palindrom
 * @head: pointer to head node of list
 *
 * Return: 1 (Palindrom) | 0 (Not a Palindrom)
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int i, values[1000];

	if (!(*head))
		return (1);

	tmp = *head, i = -1;
	while (tmp)
	{
		values[++i] = tmp->n;
		tmp = tmp->next;
	}

	tmp = *head;
	for (; i >= 0; i--)
	{
		if (values[i] != tmp->n)
			return (0);
		tmp = tmp->next;
	}

	return (1);
}

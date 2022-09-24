#include "lists.h"

/**
 * allocate_memory - allocate required memory for an array
 * @head: head node of listint_t
 *
 * Return: allocated array
 */
int *allocate_memory(listint_t *head)
{
	int *arr;
	size_t size;

	size = 0;
	while (head)
		size++, head = head->next;

	arr = malloc(sizeof(int) * size);
	if (!arr)
		exit(1);
	return (arr);
}

/**
 * is_palindrome - checks if a list is palindrom
 * @head: pointer to head node of list
 *
 * Return: 1 (Palindrom) | 0 (Not a Palindrom)
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int i, *values;

	if (!head || !(*head))
		return (1);

	values = allocate_memory(*head);
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
		{
			free(values);
			return (0);
		}
		tmp = tmp->next;
	}

	free(values);
	return (1);
}

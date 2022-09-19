#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: list's head node
 *
 * Return: 0 (no cycle) | 1 (cycle exists)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);
	slow = list, fast = list->next;
	while (fast && fast->next)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

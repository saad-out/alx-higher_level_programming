#include "lists.h"
#include <stdlib.h>

/**
 * add_head - add a node to the head of a linked list
 * @head: pointer to head node
 * @node: node to be assigned as head
 *
 * Return: pointer to node
 */
listint_t *add_head(listint_t **head, listint_t *node)
{
	node->next = *head;
	*head = node;
	return (node);
}

/**
 * insert_node - inserts node in linked list
 * @head: pointer to the head node
 * @number: number data of the node
 * Description: insert a new node at the right position in a sorted
 * linked list
 *
 * Return: new node's adress (Success) | NULL (Failure)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number, new_node->next = NULL;

	if (!(*head) || (*head)->n > number)
		return (add_head(head, new_node));

	tmp = *head;
	while (tmp && tmp->next)
	{
		if (tmp->next->n > number)
			break;
		tmp = tmp->next;
	}
	new_node->next = tmp->next;
	tmp->next = new_node;
	return (new_node);
}

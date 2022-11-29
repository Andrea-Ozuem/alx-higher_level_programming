#include "lists.h"
#include <stdio.h>

/**
  *insert_node - inserts a number into a sorted singly linked list.
  *@head: head of list
  *@number: number to be inserted
  *Return: address of new node of NULL if failed
  */
listint_t *insert_node(listint_t **head, int number)
{
	int i, j;
	listint_t *tmp, *current;

	if (*head == NULL)
		return (NULL);
	for (i = 0, tmp = *head; tmp != NULL; tmp = tmp->next, i++)
	{
		if (number < tmp->n)
			break;
	}
	for (j = 0, tmp = *head; j < i - 1 && tmp != NULL; j++)
		tmp = tmp->next;
	if (add_nodeint_end(&current, number) == NULL)
		return (NULL);
	current->next = tmp->next;
	tmp->next = current;
	return (current);
}

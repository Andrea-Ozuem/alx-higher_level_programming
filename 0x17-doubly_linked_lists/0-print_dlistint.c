#include "lists.h"

/**
  *print_dlistint - print all elements in a dlistint list
  *@h: head of list
  *Return: number of nodes
  */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *tmp;
	int i;

	for (i = 0, tmp = h; tmp; tmp = tmp->next, i++)
		printf("%d\n", tmp->n);
	return (i);
}

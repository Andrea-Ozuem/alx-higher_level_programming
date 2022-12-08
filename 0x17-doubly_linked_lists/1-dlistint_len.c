#include "lists.h"

/**
  *dlistint_len - print all elements in a dlistint list
  *@h: head of list
  *Return: number of nodes
  */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *tmp;
	int i;

	for (i = 0, tmp = h; tmp; tmp = tmp->next, i++)
		;
	return (i);
}

#include "lists.h"

/**
  *add_dnodeint - add new node at the beginning of list
  *@head: head of list
  *@n: int to be added
  *Return: address of new element else NULL
  */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *tmp = *head;
	dlistint_t *new;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	tmp->prev = new;
	new->next = tmp;
	new->prev = NULL;
	tmp = new;
	return (tmp);
}

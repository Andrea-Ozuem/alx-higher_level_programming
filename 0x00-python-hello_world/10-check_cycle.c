#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "lists.h"

/**
  *check_cycle - checks if a singly linked list has a cycle in it
  *@list: list head
  *Return: 1 if has a cycle else 0
  */
int check_cycle(listint_t *list)
{
	listint_t *p, *tmp;

	if (list == NULL)
		return (0);
	p = list;
	tmp = list;
	p = p->next;
	while (p != NULL)
	{
		if (p == tmp)
			return (1);
		p = p->next;
	}

	return (0);
}

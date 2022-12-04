#include "lists.h"
#include <stdlib.h>

/**
  *is_palindrome - checks if a singly linked list is palindrome
  *@head: list head
  *Return: 0 if not and 1 if it's a palindrome
  */
int is_palindrome(listint_t **head)
{
	int i, j;
	listint_t *tmp;
	int *arr;

	if (*head == NULL)
		return (0);
	for (i = 0, tmp = *head; tmp; tmp = tmp->next, i++)
		;
	arr = malloc(sizeof(int) * i);
	for (i = 0, tmp = *head; tmp; tmp = tmp->next, i++)
		arr[i] = tmp->n;

	for (j = i - 1, tmp = *head; j >= 0 && tmp != NULL; j--, tmp = tmp->next)
	{
		if (arr[j] != tmp->n)
			return (0);
	}
	free(arr);
	return (1);
}

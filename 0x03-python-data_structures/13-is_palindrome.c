#include "lists.h"

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_list - Reverses a singly-linked listint_t list.
 * @head: Points to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Points to the head of the linked list.
 *
 * Return: 0 - If not a palindrome.
 *         1 - If the is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmpo, *reverse, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmpo = *head;
	while (tmpo)
	{
		size++;
		tmpo = tmpo->next;
	}

	tmpo = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmpo = tmpo->next;

	if ((size % 2) == 0 && tmpo->n != tmpo->next->n)
		return (0);

	tmpo = tmpo->next->next;
	reverse = reverse_list(&tmp);
	middle = reverse;

	tmpo = *head;
	while (reverse)
	{
		if (tmpo->n != reverse->n)
			return (0);
		tmpo = tmpo->next;
		reverse = reverse->next;
	}
	reverse_list(&middle);

	return (1);
}

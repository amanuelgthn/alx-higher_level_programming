#include"lists.h"
/**
*insert_node-function that inserts a number into sorted singly linked list
*@head:a sorted singly linked list
*@number:number to be inserted into a sorted singly linked list
*Return:the address of the new inserted node or NULL if it failed
**/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;
	
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}
	
	return (new);
}

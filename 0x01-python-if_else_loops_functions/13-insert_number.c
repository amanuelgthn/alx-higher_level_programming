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
	listint_t *current, *headcurrent;
	int i = 0,j = 0;
	
	current = *head;
	headcurrent = *head;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	
	if (*head == NULL)
	{
		*head = new;
	}
	else
	{
		while (current->n < number)
		{
			current = current->next;
			i = i + 1;
		}
		while (j < i - 1 && i > 0)
		{
			headcurrent = headcurrent->next;
			j = j + 1;
		}
		if (i == 0)
		{
			new->next = *head;
		}
				
		else if (i != 0 && headcurrent->next != NULL)
		{
			new->next = headcurrent->next;
			headcurrent->next= new;
		}
		
	}
	
	return (new);
}

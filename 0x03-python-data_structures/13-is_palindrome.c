#include"lists.h"
/**
 * num_nodes - function to return number of nodes in a linked list
 * @h: pointer to head of list
 * Return: number of nodes
 */
int num_nodes(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

	current = h;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	return (n);
}
/**
 * array - function to convert a singly linked list to an array
 * @h: pointer to head of list
 * Return: converted array
 */
int *array(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;
	int len, *new_array;

	len = num_nodes(h);
	current = h;
	n = 0;
	new_array = (int *)malloc(sizeof(int) * len + 1);
	while (current != NULL)
	{
		new_array[n] = current->n;
		current = current->next;
		n++;
	}
	return (new_array);
}
/**
*check_palindrome-function to check if an array is palindrome
*@arr:array to be checked
*@start:left index
*@end:right index
*Return:1 if array is palindrome or 0 if not
**/
int check_palindrome(int arr[], int start, int end)
{
	if (start >= end)
	{
		return (1);
	}
	if (arr[start] == arr[end])
	{
		return (check_palindrome(arr, start + 1, end - 1));
	}
	else
	{
		return (0);
	}
}
/**
*is_palindrome-function to check weather a linked list is palindrome
*@head:singly linked list
*Return:1 if the singly linked list is palindrome 0 if nor
**/
int is_palindrome(listint_t **head)
{
	int check, length;
	int *new_array = array(*head);

	length = num_nodes(*head);
	check = check_palindrome(new_array, 0, length - 1);
	return (check);
}

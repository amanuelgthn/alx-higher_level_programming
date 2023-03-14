You are not allowed to google anything
Whiteboard first
Write a function in C that inserts a number into a sorted singly linked list.

Prototype: listint_t *insert_node(listint_t **head, int number);
Return: the address of the new node, or NULL if it failed
#include"lists.h"
/**
*insert_node-function that inserts a number into sorted singly linked list
*@head:a sorted singly linked list
*@number:number to be inserted into a sorted singly linked list
*Return:the address of the new inserted node or NULL if it failed
**/
listint_t *insert_node(listint_t **head, int number)

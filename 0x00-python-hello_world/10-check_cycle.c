#include "lists.h"

/**
 * addCheckedNoded - Description
 * @head: Description
 * @checkedNoded_t: Description
 * Return: Description
 */
int addCheckedNoded(checkedNoded_t **head, const listint_t *checkedNode)
{
	/* Create a new node object */
	checkedNoded_t *newNode = malloc(sizeof(checkedNoded_t));

	if (newNode == NULL)
		return (0);


	/* Init the new node */
	newNode->checkedNode = checkedNode;
	newNode->next = *head;

	/* Set the new head */
	*head = newNode;

	return (1);
}

/**
 * freeCheckedNodedList - Description
 * @head: Description
 * Return: Description
 */
void freeCheckedNodedList(checkedNoded_t **head)
{
	checkedNoded_t *currentNode = *head, *nextNode;

	while (currentNode != NULL)
	{
		nextNode = currentNode->next;

		free(currentNode);

		currentNode = nextNode;
	}
}

/**
 * nodeHasBeenChecked - Description
 * @checkedNodes: Description
 * @node: Description
 * Return: Description
 */
int nodeHasBeenChecked(checkedNoded_t *checkedNodes, const listint_t *node)
{
	const checkedNoded_t *currentNode = checkedNodes;

	while (currentNode != NULL)
	{
		if (currentNode->checkedNode == node)
			return (1);

		currentNode = currentNode->next;
	}

	return (0);
}

int check_cycle(listint_t *list)
{
	int nodes = 0;
	const listint_t *currentNode = list;
	checkedNoded_t *checkedNodes = NULL;

	while (currentNode != NULL)
	{
		/* Make sure we're not looping more than once */
		if (nodes > 0 && nodeHasBeenChecked(checkedNodes, currentNode))
		{
			freeCheckedNodedList(&checkedNodes);
			return (1);
		}

		++nodes;

		/* Save this node, since we've checked it */
		if (!addCheckedNoded(&checkedNodes, currentNode))
			exit(98);

		currentNode = currentNode->next;
	}

	freeCheckedNodedList(&checkedNodes);

	return (0);
}
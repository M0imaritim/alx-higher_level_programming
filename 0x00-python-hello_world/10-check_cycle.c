#include "lists.h"
/**
 * check_cycle - checks if linked list has a cycle
 * @list: the list
 * Return: 1 if there is a cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (!list)
		return (0);
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);

}

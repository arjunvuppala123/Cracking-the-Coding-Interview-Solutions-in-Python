#include <stdio.h>
#include <stdlib.h>

struct Node {
	int data;
	struct Node* next;
};

typedef struct Node node;

void push(struct Node** head_ref, int new_data)
{
	struct Node* new_node
		= (struct Node*)malloc(sizeof(struct Node));

	new_node->data = new_data;

	new_node->next = (*head_ref);

	(*head_ref) = new_node;
}

void printList(struct Node* node)
{
	while (node != NULL) {
		printf("%d ", node->data);
		node = node->next;
	}
}

void swapPointer(struct Node** a, struct Node** b)
{
	node* t = *a;
	*a = *b;
	*b = t;
}

int getSize(struct Node* node)
{
	int size = 0;
	while (node != NULL) {
		node = node->next;
		size++;
	}
	return size;
}

node* addSameSize(struct Node* head1,
				struct Node* head2, int* carry)
{
	if (head1 == NULL)
		return NULL;

	int sum;

	struct Node* result = (struct Node*)malloc(sizeof(struct Node));

	result->next
		= addSameSize(head1->next,
					head2->next, carry);

	sum = head1->data + head2->data + *carry;
	*carry = sum / 10;
	sum = sum % 10;

	result->data = sum;

	return result;
}

void addCarryToRemaining(struct Node* head1,
						struct Node* cur, int* carry,
						struct Node** result)
{
	int sum;

	if (head1 != cur) {
		addCarryToRemaining(head1->next,
							cur, carry,
							result);

		sum = head1->data + *carry;
		*carry = sum / 10;
		sum %= 10;

		push(result, sum);
	}
}

void addList(struct Node* head1,
			struct Node* head2, struct Node** result)
{
	struct Node* cur;

	if (head1 == NULL) {
		*result = head2;
		return;
	}

	else if (head2 == NULL)
	{
		*result = head1;
		return;
	}

	int size1 = getSize(head1);
	int size2 = getSize(head2);

	int carry = 0;

	if (size1 == size2)
		*result = addSameSize(head1, head2, &carry);

	else {
		int diff = abs(size1 - size2);

		if (size1 < size2)
			swapPointer(&head1, &head2);

		for (cur = head1; diff--; cur = cur->next)
			;

		*result = addSameSize(cur,
							head2, &carry);

		addCarryToRemaining(head1,
							cur, &carry, result);
	}

	if (carry)
		push(result, carry);
}

// Driver code
int main()
{
	struct Node *head1 = NULL, *head2 = NULL, *result = NULL;

	int arr1[] = { 9, 9, 9 };
	int arr2[] = { 1, 8 };

	int size1 = sizeof(arr1) / sizeof(arr1[0]);
	int size2 = sizeof(arr2) / sizeof(arr2[0]);

	int i;
	for (i = size1 - 1; i >= 0; --i)
		push(&head1, arr1[i]);

	for (i = size2 - 1; i >= 0; --i)
		push(&head2, arr2[i]);

	addList(head1, head2, &result);

	printList(result);

	return 0;
}

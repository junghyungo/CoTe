#include <stdio.h>
#define Min -10000
#define Max 10000

int main(void)
{
	int A, B;
	scanf("%d %d", &A, &B);
	if ((Min <= A <= Max) && (Min <= B <= Max))
		if (A < B)
			printf("<");
		else if (A > B)
			printf(">");
		else if (A == B)
			printf("==");
	return 0;
}
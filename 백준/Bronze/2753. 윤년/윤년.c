#include <stdio.h>

int main(void)
{
	int YEAR;
	scanf("%d", &YEAR);
	double a, b ,c;
	a = YEAR % 4;
	b = YEAR % 100;
	c = YEAR % 400;

	if (1 <= YEAR && YEAR <= 4000)
		if (a == 0 && b != 0)
			printf("1");
		else if (c == 0)
			printf("1");
		else
			printf("0");

	return 0;
}
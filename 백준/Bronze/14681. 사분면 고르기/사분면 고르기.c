#include <stdio.h>

int main(void)
{
	int x, y;
	scanf("%d", &x);
	scanf("%d", &y);

	if ((-1000 <= x && x <= 1000) && (-1000 <= y && y <= 1000) && (x != 0 && y != 0))
		if (0 < x && 0 < y)
			printf("1");
		else if (0 > x && 0 < y)
			printf("2");
		else if (0 > x && 0 > y)
			printf("3");
		else if (0 < x && 0 > y)
			printf("4");

	return 0;
}
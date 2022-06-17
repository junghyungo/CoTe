#include <stdio.h>

int main(void)
{
	int i, n, result = 1;
	scanf("%d", &n);
	if (1 <= n && n <= 10000)
	{
		for (i = 2; i <= n; i++)
		{
			result += i;
		}
		printf("%d", result);
	}

	return 0;
}
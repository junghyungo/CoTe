#include <stdio.h>

int main(void)
{
	int H, M;
	scanf("%d %d", &H, &M);
	if ((0 <= H && H <= 23) && (0 <= M && M <= 59))
	{
		if (45 <= M)
			M = M - 45;
		else if (0 <= M && M < 45)
		{
			M = M + 15;
			if (1 <= H && H <= 23)
				H = H - 1;
			else if (H == 0)
				H = 23;
		}
	}
	printf("%d %d", H, M);

	return 0;
}
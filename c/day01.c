#include <stdio.h>

void part1()
{
	FILE *fp;
	char c;
	int n;

	int dial;
	int password;

	dial = 50;
	password = 0;

	fp = fopen("input/day01/in.txt", "r");
	while (1) {
		if (fscanf(fp, "%c%d\n", &c, &n) != 2)
			break;

		if (c == 'R')
			dial = (dial + n) % 100;
		else
			dial = (dial - n) % 100;

		if (dial == 0)
			password++;
	}
	printf("%d\n", password);
}

void part2()
{
	FILE *fp;
	int i;
	char c;
	int n;

	int dial;
	int password;

	dial = 50;
	password = 0;

	fp = fopen("input/day01/in.txt", "r");
	while (1) {
		if (fscanf(fp, "%c%d\n", &c, &n) != 2)
			break;

		for (i = 0; i < n; ++i) {
			if (c == 'R')
				dial = (dial + 1) % 100;
			else
				dial = (dial - 1) % 100;

			if (dial == 0)
				password++;
		}
	}
	printf("%d\n", password);
}

int main()
{
	part1();
	part2();
}
